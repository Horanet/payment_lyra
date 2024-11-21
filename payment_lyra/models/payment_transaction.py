from datetime import datetime
import logging
import math

from odoo import models, api, release, fields, _
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare

from ..helpers import tools

_logger = logging.getLogger(__name__)

class TransactionLyra(models.Model):
    _inherit = 'payment.transaction'

    lyra_trans_status = fields.Char(_('Transaction status'))
    lyra_card_brand = fields.Char(_('Means of payment'))
    lyra_card_number = fields.Char(_('Card number'))
    lyra_expiration_date = fields.Char(_('Expiration date'))
    lyra_auth_result = fields.Char(_('Authorization result'))
    lyra_raw_data = fields.Text(string=_('Transaction log'), readonly=True)

    provider = fields.Char(compute='_compute_provider')

    @api.model
    def _compute_provider(self):
        for provider in self:
            provider = provider.acquirer_id.provider

    # --------------------------------------------------
    # FORM RELATED METHODS
    # --------------------------------------------------

    @api.model
    def _lyra_form_get_tx_from_data(self, data):
        shasign, status, reference = data.get('signature'), data.get('vads_trans_status'), data.get('vads_ext_info_order_ref') or data.get('vads_order_id')

        if not reference or not shasign or not status:
            error_msg = 'Lyra Collect : received bad data {}'.format(data)
            _logger.error(error_msg)
            raise ValidationError(error_msg)

        tx = self.search([('reference', '=', reference)])
        if not tx or len(tx) > 1:
            error_msg = 'Lyra Collect: received data for reference {}'.format(reference)
            if not tx:
                error_msg += '; no order found'
            else:
                error_msg += '; multiple order found'

            _logger.error(error_msg)
            raise ValidationError(error_msg)

        # Verify shasign.
        shasign_check = tx.acquirer_id._lyra_generate_sign('out', data)
        if shasign_check.upper() != shasign.upper():
            error_msg = 'Lyra Collect: invalid shasign, received {}, computed {}, for data {}'.format(shasign, shasign_check, data)
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    def _lyra_form_get_invalid_parameters(self, data):
        invalid_parameters = []

        # Check what is bought.
        amount = float(int(data.get('vads_amount', 0)) / math.pow(10, int(self.currency_id.decimal_places)))

        if float_compare(amount, self.amount, int(self.currency_id.decimal_places)) != 0:
            invalid_parameters.append(('amount', amount, '{:.2f}'.format(self.amount)))

        currency_code = tools.find_currency(self.currency_id.name)
        if (currency_code is None) or (int(data.get('vads_currency')) != int(currency_code)):
            invalid_parameters.append(('currency', data.get('vads_currency'), currency_code))

        return invalid_parameters

    def _lyra_form_validate(self, data):
        lyra_statuses = {
            'success': ['AUTHORISED', 'CAPTURED', 'ACCEPTED'],
            'pending': ['AUTHORISED_TO_VALIDATE', 'WAITING_AUTHORISATION', 'WAITING_AUTHORISATION_TO_VALIDATE', 'INITIAL', 'UNDER_VERIFICATION', 'WAITING_FOR_PAYMENT', 'PRE_AUTHORISED'],
            'cancel': ['ABANDONED']
        }

        html_3ds = _('3DS authentication: ')
        if data.get('vads_threeds_status') == 'Y':
            html_3ds += _('YES')
            html_3ds += '<br />' + _('3DS certificate: ') + data.get('vads_threeds_cavv')
        else:
            html_3ds += _('NO')

        expiry = ''
        if data.get('vads_expiry_month') and data.get('vads_expiry_year'):
            expiry = data.get('vads_expiry_month').zfill(2) + '/' + data.get('vads_expiry_year')

        values = {
            'acquirer_reference': data.get('vads_trans_uuid'),
            'lyra_raw_data': '{}'.format(data),
            'html_3ds': html_3ds,
            'lyra_trans_status': data.get('vads_trans_status'),
            'lyra_card_brand': data.get('vads_card_brand'),
            'lyra_card_number': data.get('vads_card_number'),
            'lyra_expiration_date': expiry,
        }

        # Set validation date.
        key = 'date' if hasattr(self, 'date')  else 'date_validate'
        values[key] = fields.Datetime.now()

        status = data.get('vads_trans_status')
        if status in lyra_statuses['success']:
            values.update({
                'state': 'done',
            })

            self.write(values)

            return True
        elif status in lyra_statuses['pending']:
            values.update({
                'state': 'pending',
            })

            self.write(values)

            return True
        elif status in lyra_statuses['cancel']:
            self.write({
                'state_message': 'Payment for transaction #%s is cancelled (%s).' % (self.reference, data.get('vads_result')),
                'state': 'cancel',
            })

            return False
        else:
            auth_result = data.get('vads_auth_result')
            auth_message = _('See the transaction details for more information ({}).').format(auth_result)

            error_msg = 'Lyra Collect payment error, transaction status: {}, authorization result: {}.'.format(status, auth_result)
            _logger.info(error_msg)

            values.update({
                'state_message': 'Payment for transaction #%s is refused (%s).' % (self.reference, data.get('vads_result')),
                'state': 'error',
                'lyra_auth_result': auth_message,
            })

            self.write(values)

            return False
