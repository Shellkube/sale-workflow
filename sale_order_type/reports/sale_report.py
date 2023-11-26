# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    type_id = fields.Many2one(
        comodel_name="sale.order.type",
        string="Type",
    )
    partner_invoice_id = fields.Many2one(
        comodel_name="res.partner",
        string="Invoice Address",
    )
    # flake8: noqa
    # pylint:disable=dangerous-default-value
    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["type_id"] = "s.type_id"
        res["partner_invoice_id"] = "s.partner_invoice_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """, s.type_id"""
        res += """, s.partner_invoice_id"""
        return res
