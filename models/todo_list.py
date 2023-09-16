from odoo import api, fields, models

class OwlTodo(models.Model):
    _name = 'owl.todo.list'
    _description = 'OWL Todo List'
    
    name  = fields.Char(string="Task Name")
    completed = fields.Boolean(string="Completed")
    color = fields.Char(string='Color')