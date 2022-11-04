from odoo import fields, models

class salida(models.Model):
    _name = "salidacomplejo.salida"
    _inherit= ['mail.thread','mail.activity.mixin']
    name = fields.Char(string="secuencia",readonly="True",default="New")
    contacts_id =fields.Many2one(comodel_name="res.user",string="Contacto")

