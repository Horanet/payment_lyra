# coding: utf-8
#
# Copyright © Lyra Network.
# This file is part of Lyra Collect plugin for Odoo. See COPYING.md for license details.
#
# Author:    Lyra Network (https://www.lyra.com)
# Copyright: Copyright © Lyra Network
# License:   http://www.gnu.org/licenses/agpl.html GNU Affero General Public License (AGPL v3)

from odoo import _

# WARN: Do not modify code format here. This is managed by build files.
LYRA_PLUGIN_FEATURES = {
    'multi': True,
    'restrictmulti': False,
    'qualif': False,
    'shatwo': True,
}

LYRA_PARAMS = {
    'GATEWAY_CODE': 'Lyra',
    'GATEWAY_NAME': 'Lyra Collect',
    'BACKOFFICE_NAME': 'Lyra Expert',
    'SUPPORT_EMAIL': 'support-ecommerce@lyra-collect.com',
    'GATEWAY_URL': 'https://secure.lyra.com/vads-payment/',
    'SITE_ID': '12345678',
    'KEY_TEST': '1111111111111111',
    'KEY_PROD': '2222222222222222',
    'CTX_MODE': 'TEST',
    'SIGN_ALGO': 'SHA-256',
    'LANGUAGE': 'en',

    'GATEWAY_VERSION': 'V2',
    'PLUGIN_VERSION': '1.2.6',
    'CMS_IDENTIFIER': 'Odoo_10-14',
}

LYRA_LANGUAGES = {
    'cn': 'Chinese',
    'de': 'German',
    'es': 'Spanish',
    'en': 'English',
    'fr': 'French',
    'it': 'Italian',
    'jp': 'Japanese',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'sv': 'Swedish',
    'tr': 'Turkish',
}

LYRA_CARDS = {
            'CB': u'CB',
    'E-CARTEBLEUE': u'e-Carte Bleue',
    'MAESTRO': u'Maestro',
    'MASTERCARD': u'Mastercard',
            'VISA': u'Visa',
    'VISA_ELECTRON': u'Visa Electron',
    'VPAY': u'V PAY',
    'AMEX': u'American Express',
            'ACCORD_STORE': u'Cartes Enseignes Partenaires',
    'ACCORD_STORE_SB': u'Cartes Enseignes Partenaires (sandbox)',
            'ALINEA': u'Carte myalinea',
    'ALINEA_CDX': u'Carte Cadeau Alinéa',
    'ALINEA_CDX_SB': u'Carte Cadeau Alinéa (sandbox)',
            'ALINEA_SB': u'Carte myalinea (sandbox)',
    'ALIPAY': u'Alipay',
    'ALLOBEBE_CDX': u'Carte Cadeau Allobébé',
            'ALLOBEBE_CDX_SB': u'Carte Cadeau Allobébé (sandbox)',
    'ALMA': u'Alma en 1 fois',
    'ALMA_10X': u'Alma in 10 installments',
            'ALMA_12X': u'Alma in 12 installments',
    'ALMA_2X': u'Alma in 2 installments',
    'ALMA_3X': u'Alma in 3 installments',
            'ALMA_4X': u'Alma in 4 installments',
    'APETIZ': u'Apetiz',
    'APPLE_PAY': u'Apple Pay',
            'AUCHAN': u'Carte Auchan',
    'AUCHAN_SB': u'Carte Auchan (sandbox)',
    'AURORE-MULTI': u'Cpay Aurore',
            'BANCONTACT': u'Bancontact Mistercash',
    'BIZUM': u'Bizum',
    'BIZZBEE_CDX': u'Carte Cadeau Bizzbee',
            'BIZZBEE_CDX_SB': u'Carte Cadeau Bizzbee (sandbox)',
    'BOULANGER': u'Carte b+',
    'BOULANGER_SB': u'Carte b+ (sandbox)',
            'BRICE_CDX': u'Carte Cadeau Brice',
    'BRICE_CDX_SB': u'Carte Cadeau Brice (sandbox)',
    'BUT': u'But',
            'CABAL': u'Cabal',
    'CARNET': u'Carnet',
    'CA_DO_CARTE': u'CA DO Carte',
    'CHQ_DEJ': u'Chèque Déjeuner',
            'COM_BARRY_CDX': u'Carte Cadeau Comtesse du Barry',
    'COM_BARRY_CDX_SB': u'Carte Cadeau Comtesse du Barry (sandbox)',
            'CONECS': u'Conecs',
    'CONFORAMA': u'Conforama',
    'CORA': u'Cora',
    'CORA_BLANCHE': u'Cora blanche',
            'CORA_PREM': u'Cora Visa Premier',
    'CORA_VISA': u'Cora Visa',
    'CVCO': u'Chèque-Vacances Connect',
            'DINERS': u'Diners',
    'DISCOVER': u'Discover',
    'ECCARD': u'EC Card',
    'EDENRED': u'Ticket Restaurant',
            'EDENRED_EC': u'Ticket EcoCheque',
    'EDENRED_SC': u'Ticket Sport & Culture',
            'EDENRED_TC': u'Ticket Compliments',
    'EDENRED_TR': u'Ticket Restaurant',
    'ELO': u'Elo',
            'FRANFINANCE_3X': u'Paiement en 3 fois',
    'FRANFINANCE_4X': u'Paiement en 4 fois',
            'FULLCB3X': u'Paiement en 3 fois CB',
    'FULLCB4X': u'Paiement en 4 fois CB',
    'GEMO_CDX': u'Carte Cadeau Gémo',
            'GEMO_CDX_SB': u'Carte Cadeau Gémo (sandbox)',
    'GIROPAY': u'Giropay',
    'HIPER': u'Hiper',
            'HIPERCARD': u'Hipercard',
    'IDEAL': u'iDEAL',
    'ILLICADO': u'Carte Illicado',
            'ILLICADO_SB': u'Carte Illicado (sandbox)',
    'IP_WIRE': u'Virement SEPA',
    'IP_WIRE_INST': u'Virement SEPA Instantané',
            'JCB': u'JCB',
    'JOUECLUB_CDX': u'Carte Cadeau Joué Club',
    'JOUECLUB_CDX_SB': u'Carte Cadeau Joué Club (sandbox)',
            'JULES_CDX': u'Carte Cadeau Jules',
    'JULES_CDX_SB': u'Carte Cadeau Jules (sandbox)',
            'KADEOS_CULTURE': u'Carte Kadéos Culture',
    'KADEOS_GIFT': u'Carte Kadéos Zénith',
    'LECLERC': u'Carte Reglo',
            'LEROY-MERLIN': u'Carte Maison Financement',
    'LEROY-MERLIN_SB': u'Carte Maison Financement (sandbox)',
            'MASTERPASS': u'MasterPass',
    'MC_CORDOBESA': u'Mastercard Cordobesa',
    'MULTIBANCO': u'Multibanco',
            'MYBANK': u'MyBank',
    'NARANJA': u'Naranja',
    'NORAUTO': u'Carte Norauto option Financement',
            'NORAUTO_SB': u'Carte Norauto option Financement (sandbox)',
    'ONEY_10X_12X': u'Paiement en 10 ou 12 fois Oney',
            'ONEY_3X_4X': u'Paiement en 3 ou 4 fois Oney',
    'ONEY_ENSEIGNE': u'Cartes enseignes Oney',
            'ONEY_PAYLATER': u'Pay Later Oney',
    'PAYCONIQ': u'Payconiq',
    'PAYDIREKT': u'Paydirekt',
    'PAYPAL': u'PayPal',
            'PAYPAL_SB': u'PayPal Sandbox',
    'PICWIC': u'Carte Picwic',
    'PICWIC_SB': u'Carte Picwic (sandbox)',
            'POSTFINANCE': u'PostFinance Card',
    'POSTFINANCE_EFIN': u'PostFinance E-Finance',
    'PRESTO': u'Presto',
            'PRZELEWY24': u'Przelewy24',
    'S-MONEY': u'S-money',
    'SCT': u'Virement SEPA',
    'SDD': u'SEPA direct debit',
            'SODEXO': u'Pass Restaurant',
    'SOFORT_BANKING': u'Sofort',
    'SOROCRED': u'Sorocred',
    'UNION_PAY': u'UnionPay',
            'UPI': u'UPI',
    'VILLAVERDE': u'Carte Cadeau VillaVerde',
    'VILLAVERDE_SB': u'Carte Cadeau VillaVerde (sandbox)',
    'WECHAT': u'WeChat Pay',
}

LYRA_CURRENCIES = [
            ['CAD', '124', 2],
    ['CHF', '756', 2],
    ['DKK', '208', 2],
    ['EUR', '978', 2],
            ['GBP', '826', 2],
    ['JPY', '392', 0],
    ['NOK', '578', 2],
    ['PLN', '985', 2],
            ['SEK', '752', 2],
    ['USD', '840', 2],
]
