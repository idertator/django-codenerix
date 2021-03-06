__version__ = "1.0.27"

__authors__ = [
    'Juan Miguel Taboada Godoy <juanmi@juanmitaboada.com>',
    'Juan Soler Ruiz <soleronline@gmail.com>',
    'Francisco Torrejon Puente <frantorrejon@gmail.com>',
]

__requirements__ = {
    '2':[
        "pymongo",
        "django-angular",
        "python-dateutil",
        "django-recaptcha>=1.2.1,<1.3",
        "django-rosetta",
        "jsonfield",
        "openpyxl",
        "Pillow",
        "Unidecode",
        "xhtml2pdf",
        "html5lib==1.0b8", # Default version 0.99999999 is broken with error 'from html5lib import treebuilders, inputstream' => 'ImportError: cannot import name inputstream' (1.0b10 also fails)
        "Django>=1.10.6,<1.11",
        "django-multi-email-field",
        "ldap3",
    ],
    '3':[
        "pymongo",
        "django-angular",
        "python-dateutil",
        "django-recaptcha>=1.2.1,<1.3",
        "django-rosetta",
        "jsonfield",
        "openpyxl",
        "Pillow",
        "Unidecode",
        "xhtml2pdf",
        "html5lib",
        "Django>=1.10.6,<1.11",
        "django-multi-email-field",
        "ldap3",
        ],
    }
