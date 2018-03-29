# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import jinja2

path = 'C:/Users/lei/Desktop/project/export/doc/'
fsl = jinja2.FileSystemLoader(searchpath=path)

env = jinja2.Environment(loader=fsl)
tpl = env.get_template("test.xml")

data = {
    'name': '这是一个测试',
    'ip': '10.10.10.66',
    'status': '正在进行中......',
    'start_time': '2018-3-28',
    'end_time': '2018-3-29',
    'time': '2018-3-29 123213212321',
    'num': '10000000'
}

with open(path + "test.doc", 'w') as f:
    f.write(tpl.render(data = data).encode('utf-8'))

