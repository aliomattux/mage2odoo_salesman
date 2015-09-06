from openerp.osv import osv, fields
from pprint import pprint as pp

class SaleOrder(osv.osv):
    _inherit = 'sale.order'
    _columns = {
	'account_number': fields.char('Account Number'),
	'account_name': fields.char('Account Name'),
	'custom_account': fields.boolean('Custom Account'),
	'service': fields.many2one('delivery.carrier', 'Service', \
		domain=[('mage_carrier_code', 'in', ['ups', 'fedex']), ('display_in_ui', '=', True)]
	),
	'account_zipcode': fields.char('Account Zipcode'),
    }



    def onchange_carrier_id(self, cr, uid, ids, carrier_id, billing_address_id, context=None):
        defaults = {'custom_account': False, 'account_number': False, 'account_name': False, 'service': False}

        if not carrier_id:
	    return {'value': defaults}

	carrier = self.pool.get('delivery.carrier').browse(cr, uid, carrier_id)
	billing_address = self.pool.get('res.partner').browse(cr, uid, billing_address_id)
	defaults['custom_account'] = carrier.custom_account
	defaults ['account_name'] = billing_address.name
	defaults['account_zipcode'] = billing_address.zip

        return {'value': defaults}
