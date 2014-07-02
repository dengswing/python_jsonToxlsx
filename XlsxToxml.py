#-*- coding: utf8 -*-
import xlrd
import json
import xml.dom.minidom

fname = "text2.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)


def findTemp(key,tData):
	isFind=0
	for k in tData:
		if k == key:
			isFind=1
			break
	return isFind
	
	
jObj={}
tTitle=[]
tChild=[]
tContent=[]
for i in range(1,nrows):
	sKey=sh.cell_value(i,0)
	aList=sKey.split('>')
	
	if findTemp(aList[0],tTitle) == 0:
		jObj[aList[0]]={}
		tTitle.append(aList[0])
		
	if findTemp(aList[0]+"_"+aList[2],tChild) == 0:
		jObj[aList[0]][aList[2]]={}
		tChild.append(aList[0]+"_"+aList[2])
		
	if findTemp(aList[0]+"_"+aList[2]+"_"+aList[3],tContent) == 0:
		jObj[aList[0]][aList[2]][aList[3]]={}
		tContent.append(aList[0]+"_"+aList[2]+"_"+aList[3])
	
	jObj[aList[0]][aList[2]][aList[3]] = sh.cell_value(i,1) 
	
def generateXml(sName,data):
	impl = xml.dom.minidom.getDOMImplementation()
	dom = impl.createDocument(None, 'data', None) 
	root = dom.documentElement 
	
	for a in data:
		employee = dom.createElement(a)
		root.appendChild(employee)
		nameE = dom.createElement("info")
		employee.appendChild(nameE)
		for b in data[a]:			
			nameE.setAttribute(b,data[a][b])
  
	f= open(sName+'_new.xml', 'w')
	f.write(dom.toprettyxml(encoding = 'utf-8'))
	f.close()

	
for s in jObj:
	generateXml(s,jObj[s])
	
print "finish create"	


