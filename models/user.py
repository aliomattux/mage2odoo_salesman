from openerp.osv import osv, fields


class ResUsers(osv.osv):
    _inherit = 'res.users'
    _columns = {
        'external_id': fields.integer('External Id'),
        
    }


    def get_or_create_odoo_record(self, cr, uid, job, record, context=None):
	if not record:
	    return False
	external_id = record.get('user_id')
	if not external_id:
	    return False

	user_ids = self.search(cr, uid, [('external_id', '=', external_id)])
	if user_ids:
	    return user_ids[0]
	else:
	    vals = self.prepare_odoo_record_vals(cr, uid, job, record)
	    return self.create(cr, uid, vals)


    def prepare_odoo_record_vals(self, cr, uid, job, record, context=None):
        vals = {
		'external_id': record['user_id'],
		'login': record['email'],
		'name': ' '.join([record['firstname'], record['lastname']]),
		'active': True,
	}

	return vals
