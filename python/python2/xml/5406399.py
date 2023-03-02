from xml.dom.minidom import parse
doc  = "./5406399.xml"
f = open(doc.decode('utf-8').encode('gb2312','r'))
xmldoc = parse(f)
print xmldoc.toxml()
