# -*- coding:utf-8 -*-
import pdfkit
import jinja2


TemplateLoader = jinja2.FileSystemLoader(searchpath='C:/Users/lei/Desktop/project/export/')
env = jinja2.Environment(loader=TemplateLoader)
template = env.get_template('666.html')

mock = {
    'ip': [
        '10.10.10.1',
        '10.10.10.2',
        '10.10.10.3'
    ],
    'details': {
        '10.10.10.1': {
            'info': {
                'critical': 0,
                'high': 0,
                'medium': 2,
                'low': 3,
                'info': 5
            },
            'details': [
                [
                    'Medium',
                    9.9,
                    6666,
                    'hahahah'
                ],
                [
                    'Info',
                    6.6,
                    2333,
                    '6666666'
                ]
            ]

        },
        '10.10.10.2': {
            'info': {
                'critical': 9,
                'high': 0,
                'medium': 7,
                'low': 3,
                'info': 5
            },
            'details': [
                [
                    'Medium',
                    9.9,
                    6666,
                    'hahahah'
                ],
                [
                    'Info',
                    6.6,
                    2333,
                    '6666666'
                ]
            ]

        },
        '10.10.10.3': {
            'info': {
                'critical': 1,
                'high': 0,
                'medium': 3,
                'low': 3,
                'info': 6
            },
            'details': [
                [
                    'Medium',
                    9.9,
                    6666,
                    'hahahah'
                ],
                [
                    'Info',
                    6.6,
                    2333,
                    '6666666'
                ]
            ]
        }
    }
}

options = {
    'page-size': 'Letter',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    # 在页脚显示一条横线
    # 'footer-line': None,
    # 在页眉显示一条横线
    # 'header-line': None,

    # 使用html作为页眉页脚
    # 'header-html': '',
    # 'footer-html': '',
}

result = template.render(name="这是一个测试".decode("utf-8"), mock=mock)

source_file = 'C:/Users/lei/Desktop/project/export/test.html'
out_file = 'C:/Users/lei/Desktop/project/export/test.pdf'

with open(source_file, 'w') as f:
    f.write(result.encode('utf-8'))

pdfkit.from_file(source_file, out_file, options=options)
