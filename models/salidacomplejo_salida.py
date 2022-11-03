from odoo import fields, models

class salida(models.Model):
    _name = "salidacomplejo.salida"
    name = fields.Char(string="secuencia",readonly="True")

