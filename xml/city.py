from xml.dom.minidom import parse
xmldoc = parse("./5406399.xml")
print xmldoc.toxml()
