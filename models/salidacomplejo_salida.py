from odoo import fields, models, api

class salida(models.Model):
    _name = "salidacomplejo.salida"
    _description = "Salida del Complejo"
    _inherit= ['mail.thread','mail.activity.mixin']
    name = fields.Char(string="secuencia",readonly="True",default="New")
    contacts_id =fields.Many2one(comodel_name="res.partner",string="Destino")
    direccion = fields.Char(related="contacts_id.contact_address",string="Direccion")
    solicitante = fields.Many2one(comodel_name="hr.employee", string="Solicitante")
    cargo = fields.Char(related="solicitante.job_id.display_name", string="Cargo")
    empresa = fields.Many2one(comodel_name="res.company", string="Compañia")
    @api.model
    def create(self,vals):
        if vals.get('name','New') == "New":
            vals['name']=self.env['ir.sequence'].next_by_code('code_sc_1') or "New"
        result = super(salida,self).create(vals)
        return result