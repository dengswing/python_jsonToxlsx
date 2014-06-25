#-*- coding: utf8 -*-
import xlrd
import json

fname = "text.xlsx"
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

row_list = []

jObj = {}
for i in range(1,nrows):	
    jObj[int(sh.cell_value(i,0))] = sh.cell_value(i,1)
print jObj	

print "finish create"	

file = open('textNew.json', 'w')
file.write(json.dumps(jObj))
file.close()