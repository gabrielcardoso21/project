# Copyright 2021 Gabriel Cardoso de Faria <gacarfaria@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Project Searchpanel',
    'summary': """
        Add searchpanel to project task kanban view""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Gabriel Cardoso de Faria,Odoo Community Association (OCA)',
    'website': 'https://github.com/gabrielcardoso21',
    'depends': [
        'project_category',
        'web_view_searchpanel',
    ],
    'data': [
        'views/project_task_view.xml',
    ],
    'demo': [
    ],
}
