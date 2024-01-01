# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-23 22:50
"""
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花贬低看</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大枪</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick id="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id='ppc'>胖胖陈</nick>
        <nick id='ppbc'>胖胖不陈</nick>
    </partner>
    </book>
"""
et  = etree.XML(xml)
# result = et.xpath('/book') # / 表示根节点
# result = et.xpath('/book/name') # 在xpath中间的/表示儿子
# result = et.xpath('/book/name/text()') # text() 拿文本
# result  = et.xpath('/book//nick') # //表示子孙后代
# result = et.xpath('/book/*/nick')
# result = et.xpath('/book/*/nick/text()')
# result = et.xpath('/book/author/nick[@class="joy"]/text()') # []表示属性筛选，@属性名=值
result = et.xpath('/book/partner/nick/@id')
print(result)

