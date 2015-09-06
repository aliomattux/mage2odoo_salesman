from openerp.osv import osv, fields
from openerp.tools.translate import _

class DeliveryCarrier(osv.osv):
    _inherit = 'delivery.carrier'
    _order = 'display_order'
    _columns = {
	'display_order': fields.integer('Display Order', help="This determines the order in which options are presented"),
	'custom_account': fields.boolean('Allow Custom Account Information'),
    }


