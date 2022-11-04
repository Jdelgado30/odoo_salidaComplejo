from odoo import fields, models, api

class salida(models.Model):
    _name = "salidacomplejo.salida"
    _inherit= ['mail.thread','mail.activity.mixin']
    name = fields.Char(string="secuencia",readonly="True",default="New")
    contacts_id =fields.Many2one(comodel_name="res.partner",string="Contacto")
    direccion = fields.Char(related="contacts_id.contact_address",string="Direccion")

    @api.model
    def create(self,vals):
        if vals.get('name','New') == "New":
            vals['name']=self.env['ir.sequence'].next_by_code('code_sc_1') or "New"
        result = super(salida,self).create(vals)
        return result