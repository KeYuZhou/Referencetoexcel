import xlwt
import sys
from pdfminer.high_level import extract_text
arg=sys.argv
excelname="reference.xls"
if(len(arg)==1):
    print("no pdf name")
if(len(arg)==3):
    excelname=arg[2]
pdfname=arg[1]
text = extract_text(pdfname)
txt=text.split("References\n\n")[1]
txt=txt.replace("\n","")
refer=txt.split("[")
del refer[0]
Excel = xlwt.Workbook()
table = Excel.add_sheet('Sheet1', cell_overwrite_ok=True)
for i in range(len(refer)):
    table.write(i, 0, '['+refer[i])
Excel.save(r'excelname')
