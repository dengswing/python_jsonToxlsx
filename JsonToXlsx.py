import json
try:
    import xlsxwriter
except ImportError:
    print('''
Warning: xlsxwriter library is not installed, cannot output xlsx format.
Download it from: https://pypi.python.org/pypi/XlsxWriter ''')

file = open('text.json', 'r')
data = json.load(file)

print(data)

workbook = xlsxwriter.Workbook('text.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

worksheet.write(0, 0, "ID",bold)
worksheet.write(0, 1, "text",bold)
j=0
for i in data:
	j=int(i)
	worksheet.write(j, 0, j,bold)
	worksheet.write(j, 1, data[i])
	
workbook.close()
print("finish create")