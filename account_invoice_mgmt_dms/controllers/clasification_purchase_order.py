# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, content_disposition
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression
import json
import os
import base64


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self):
        values = super(CustomerPortal, self)._prepare_home_portal_values()
        partner = request.env.user.partner_id

        purchase_id = request.env['purchase.order'].sudo().search([('partner_id', '=', partner.id), ('invoice_status_ext', '=', 'to invoice')])
        classification_purchase_ids = request.env["stock.picking.classification"].sudo().search([("picking_id.classification_purchase_order_id", "in", purchase_id.ids)]).picking_id.classification_purchase_order_id

        values.update({
            'classification_purchase_count': len(classification_purchase_ids),
        })
        return values

    @http.route(['/my/classification/purchase/', '/my/classification/purchase/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_classification_purchase_tree(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id

        searchbar_sortings = {
            'date_start': {'label': _('Date Start'), 'order': 'date_start desc'},
            'date_end': {'label': _('Date End'), 'order': 'date_end desc'},
        }

        if not sortby:
            sortby = 'date_start'
        sort_order = searchbar_sortings[sortby]['order']

        archive_groups = self._get_archive_groups('purchase.order', [('partner_id', '=', partner.id)]) if values.get('my_details') else []

        items_count = len(request.env['purchase.order'].sudo().search([('partner_id', '=', partner.id)]))

        pager = portal_pager(
            url="/my/classification/purchase",
            url_args={'date_begin': date_begin, 'date_end': date_end},
            total=items_count,
            page=page,
            step=30
        )

        purchase_id = request.env['purchase.order'].sudo().search([('partner_id', '=', partner.id), ('invoice_status_ext', '=', 'to invoice')])
        items = request.env["stock.picking.classification"].sudo().search([("picking_id.classification_purchase_order_id", "in", purchase_id.ids)]).picking_id.classification_purchase_order_id


        values.update({
            'date': date_begin,
            'items': items.sudo(),
            'page_name': 'classification_purchase',
            'archive_groups': archive_groups,
            'default_url': '/my/classification/purchase',
            'sortby': sortby,
        })
        return request.render("account_invoice_mgmt_dms.portal_my_clasification_purchase_tree", values)

    @http.route(['/my/classification/purchase/<int:order_id>'], type='http', auth="user", website=True)
    def portal_my_classification_purchase_form(self, order_id=None, **kw):
        values = self._prepare_portal_layout_values()

        purchase_id = request.env['purchase.order'].sudo().browse(order_id)
        directory_id = request.env.ref('account_invoice_mgmt_dms.dms_directory_puchase_invoice').id
        ticket_id = request.env["stock.picking.classification"].sudo().search([("picking_id.classification_purchase_order_id", "=", purchase_id.id)]).picking_id
        dms_file_id = request.env['dms.file'].sudo().search([('proceeding', '=', ticket_id.name), ('directory_id', '=', directory_id)])

        values.update({
            'item': purchase_id.sudo(),
            'dms_file': dms_file_id.sudo(),
            'page_name': 'classification_purchase_id',
            'default_url': '/my/classification/purchase/%s' % purchase_id.id,
        })
        return request.render("account_invoice_mgmt_dms.portal_my_clasification_purchase_form", values)

    @http.route(['/classification/purchase/add_attachment'], type='http', auth="public", website=True, sitemap=False)
    def portal_my_classification_purchase_upload_file(self, **post):
        if post.get('attachment', False):
            purchase_id = request.env['purchase.order'].browse(int(post.get('purchase_order')))
            ticket_id = request.env["stock.picking.classification"].sudo().search([("picking_id.classification_purchase_order_id", "=", purchase_id.id)]).picking_id.move_ids_without_package
            directory_id = request.env.ref('account_invoice_mgmt_dms.dms_directory_puchase_invoice').id

            extension_name = post.get('attachment').filename.split(".")[-1]
            extension_size = -(len(extension_name)) - 1
            name = post.get('attachment').filename[:extension_size]
            file = post.get('attachment')
            attachment = file.read()

            dms_file_id = request.env['dms.file'].sudo().create({
                'name': '%s_%s.%s' % (name, (purchase_id.name).replace("/", ""), extension_name),
                'directory_id': directory_id,
                'content': base64.b64encode(attachment),
                'proceeding': ticket_id.picking_id.name,
            })

            parent_folder = (_("/Reports/Purchase Invoices/"))
            try:
                os.makedirs(parent_folder)
            except OSError:
                # In the case that the folders already exist
                pass
            path_invoice = '%s%s.%s' % (parent_folder, name, extension_name)
            with open(path_invoice, "wb") as fh:
                fh.write(dms_file_id.content)

            return request.redirect('/my/classification/purchase/%s' % purchase_id.id)
