from odoo import models

class MyCustomReport(models.AbstractModel):
    _name = 'report.my_custom_report.report_my_custom_pdf'
    _description = 'Custom PDF Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['my.custom.report'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'my.custom.report',
            'docs': docs,
        }
