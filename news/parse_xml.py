# -*- coding: utf-8 -*-
from load_files import xmldata
#import xml.etree.ElementTree as ET
from lxml import etree

tree = etree.parse(xmldata) # Парсинг строки
#tree = etree.parse('1.xml') # Парсинг файла

nodes = tree.xpath('/items/item/headline/value') # Открываем раздел
for node in nodes: # Перебираем элементы
    # print node.tag,node.keys(),node.values()
    # print 'name =',node.get('name') # Выводим параметр name
     print('text =',[node.text]) # Выводим текст элемента