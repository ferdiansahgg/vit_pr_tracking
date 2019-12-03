from odoo import models, fields, api, _

class tracking(models.Model):

    _name = "purchase.order.line"

    _inherit = "purchase.order.line"