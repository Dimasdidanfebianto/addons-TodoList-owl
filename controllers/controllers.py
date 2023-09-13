# -*- coding: utf-8 -*-
# from odoo import http


# class TodoListApp(http.Controller):
#     @http.route('/todo_list_app/todo_list_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_list_app/todo_list_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_list_app.listing', {
#             'root': '/todo_list_app/todo_list_app',
#             'objects': http.request.env['todo_list_app.todo_list_app'].search([]),
#         })

#     @http.route('/todo_list_app/todo_list_app/objects/<model("todo_list_app.todo_list_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_list_app.object', {
#             'object': obj
#         })
