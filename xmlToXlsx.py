import xlsxwriter
from  xml.dom import  minidom

def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []
	
sObj={}	
def get_xml_data(filename='explain.xml'):
	sName=filename[:-4]
	doc = minidom.parse(filename) 
	root = doc.documentElement	
	children=root.childNodes 
	print(root.nodeName)
	for node in children:
		if node.nodeType==root.ELEMENT_NODE: 		
			#print(node.nodeName)
			childrenIn=node.childNodes
			for nodeIn in childrenIn:
				if nodeIn.nodeType==root.ELEMENT_NODE: 
					for attr in nodeIn.attributes.values():
						#print(attr.name+"="+attr.value)
						sObj[sName+">"+root.nodeName+">"+node.nodeName+">"+attr.name] = attr.value

						
get_xml_data("explain.xml")
get_xml_data("language.xml")
#print(sObj)

workbook = xlsxwriter.Workbook('text2.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

worksheet.write(0, 0, "ID",bold)
worksheet.write(0, 1, "text",bold)
j=1
for i in sObj:	
	worksheet.write(j, 0, i,bold)
	worksheet.write(j, 1, sObj[i])
	j+=1
	
workbook.close()
print("finish create")

