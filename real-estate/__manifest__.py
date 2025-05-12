{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': 'Your Name',
    'category': 'Sales',
    'summary': 'Manage real estate properties and offers',
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'data/demo_data.xml'
    ],
    'installable': True,
    'application': True,
}
