import xml.etree.ElementTree as ET
tree = ET.parse('static/Cars.xml')
root = tree.getroot()

# import xml.dom.minidom as minidom


# docs = minidom.parse('static/Cars.xml')


# idnya = docs.getElementsByTagName('Id')

# for idn in idnya[1:]:
# 	print(idn.firstChild.data)

# namanya = docs.getElementsByTagName('Name')
# for namae in namanya[1:]:
# 	print(namae.firstChild.data)


# pricenya = docs.getElementsByTagName('Price')
# for pricee in pricenya[1:]:
# 	print(pricee.firstChild.data)