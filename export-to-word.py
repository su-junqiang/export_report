# -*- coding:utf-8 -*-
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from PIL import Image


path = 'C:/Users/lei/Desktop/project/export/test/'
doc = DocxTemplate(path + 'test.docx')

# 表格循环
context = {
    'col_labels': ['水果'.decode('utf-8'), '蔬菜'.decode('utf-8'), '石头'.decode('utf-8'), '哈哈'.decode('utf-8')],
    'tbl_contents': [
        {'label': '黄色'.decode('utf-8'), 'cols': ['香蕉'.decode('utf-8'), '辣椒'.decode('utf-8'), '黄铁矿'.decode('utf-8'), '出租车'.decode('utf-8')]},
        {'label': '红色'.decode('utf-8'), 'cols': ['苹果'.decode('utf-8'), '番茄'.decode('utf-8'), '朱砂'.decode('utf-8'), '不知道'.decode('utf-8')]},
        {'label': '绿色'.decode('utf-8'), 'cols': ['青椒'.decode('utf-8'), '黄瓜'.decode('utf-8'), '茄子'.decode('utf-8'), '丝瓜'.decode('utf-8')]},
        {'label': '绿色'.decode('utf-8'), 'cols': ['青椒'.decode('utf-8'), '黄瓜'.decode('utf-8'), '茄子'.decode('utf-8'), '丝瓜'.decode('utf-8')]},
        {'label': '绿色'.decode('utf-8'), 'cols': ['青椒'.decode('utf-8'), '黄瓜'.decode('utf-8'), '茄子'.decode('utf-8'), '丝瓜'.decode('utf-8')]},
        {'label': '绿色'.decode('utf-8'), 'cols': ['青椒'.decode('utf-8'), '黄瓜'.decode('utf-8'), '茄子'.decode('utf-8'), '丝瓜'.decode('utf-8')]},
        {'label': '绿色'.decode('utf-8'), 'cols': ['青椒'.decode('utf-8'), '黄瓜'.decode('utf-8'), '茄子'.decode('utf-8'), '丝瓜'.decode('utf-8')]}
    ]
}

# 图片添加, 可以直接传路径, 也可以使用文件对象
img = open(path + 'test.png', 'rb')

context = {
    'myimage': InlineImage(doc, img, width=Mm(20))
}

doc.render(context)
doc.save(path+'hhh.docx')