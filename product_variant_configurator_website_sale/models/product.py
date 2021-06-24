from odoo.addons.http_routing.models.ir_http import slug
from odoo import _, api, fields, models

class Product(models.Model):
    _inherit = "product.product"

    @api.depends_context('lang')
    @api.depends('product_tmpl_id.website_url', 'product_template_attribute_value_ids')
    def _compute_product_website_url(self):
        for product in self:
            if product.id.__class__ != models.NewId:
                attributes = ','.join(str(x) for x in product.product_template_attribute_value_ids.ids)
                product.website_url = "%s#attr=%s" % (product.product_tmpl_id.website_url, attributes)
            else:
                product.website_url = False
