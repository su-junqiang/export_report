# -*- coding:utf-8 -*-

import jinja2


TemplateLoader = jinja2.FileSystemLoader(searchpath='C:/Users/lei/Desktop/project/export/')
env = jinja2.Environment(loader=TemplateLoader)
template = env.get_template('template.html')

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

result = template.render(name="这是一个测试".decode("utf-8"), mock=mock)

with open('C:/Users/lei/Desktop/project/export/test.html', 'w') as f:
    f.write(result.encode('utf-8'))

print "ok........."
