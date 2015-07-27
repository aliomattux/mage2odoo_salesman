from openerp.osv import osv, fields
from pprint import pprint as pp

class SaleOrder(osv.osv):
    _inherit = 'sale.order'

    def prepare_odoo_record_vals(self, cr, uid, job, record, storeview=False):
	vals = super(SaleOrder, self).prepare_odoo_record_vals(cr, uid, job, record, storeview=storeview)
	if record.get('user_data'):
	    user_obj = self.pool.get('res.users')
	    vals['user_id'] = user_obj.get_or_create_odoo_record(cr, uid, job, record)

	return vals
