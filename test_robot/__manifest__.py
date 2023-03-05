# -*- coding: utf-8 -*-
{
    'name': "Game Simulator",

    'summary': """Game Toy Simulator""",

    'description': """
        Game toys Simulator.
    """,

    'author': "Andi Rahman",
    'website': ".",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/toy_sims_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],
}
