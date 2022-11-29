#!/usr/bin/env python

#coding=utf-8

import xml.dom.minidom


dom = xml.dom.minidom.parse('abc.xml')


root = dom.documentElement

print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
