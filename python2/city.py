#!/usr/bin/python
import xml.dom.minidom

def get_citys():
        city_xml = open(os.path.join(os.path.normpath(os.path.dirname(__file__)),'city.xml'))
	doc = xml.dom.minidom.parse(city_xml)
	citys = []
	provinces = doc.getElementsByTagName('province')
	for item in provinces:
	entry = {'province':'','citys':[]}
	province = item.getAttribute('name')
	entry['province'] = province
	for city in item.getElementsByTagName('city'):
	city = city.getAttribute('name')
	entry['citys'].append(city)
	citys.append(entry)
	return citys
