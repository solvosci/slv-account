from odoo import http, _
from odoo.http import request
import base64
import io
import zipfile


class Binary(http.Controller):

    @http.route('/account_invoice_mgmt_dms/download_purchase_invoice', type='http', auth="user")
    def download_purchase_invoice(self, ids, **kw):
        list_ids = list(map(int, ids.split(',')))
        invoice_ids = request.env['account.move'].browse(list_ids)

        with io.BytesIO() as zip_buffer:
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for record in invoice_ids.filtered(lambda x: x.purchase_invoice_proceesing_id):
                    binary_data = record.purchase_invoice_proceesing_id.content
                    decoded_data = base64.b64decode(binary_data)
                    file_name = record.name.replace("/", "_")
                    zip_file.writestr(f"{file_name}.pdf", decoded_data)

            zip_buffer.seek(0)
            zip_data = zip_buffer.read()

        return request.make_response(zip_data, [('Content-Type', 'application/zip'), ('Content-Disposition', 'attachment; filename=%s.zip' % _('invoice_files'))])
