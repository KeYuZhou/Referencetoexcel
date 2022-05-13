import xlwt
from pdfminer.high_level import extract_text
text = extract_text('Single-Stage Monocular 3D Object Detection via Keypoint Estimation.pdf')
txt=text.split("References\n\n")[1]
txt=txt.replace("\n","")
refer=txt.split("[")
del refer[0]
Excel = xlwt.Workbook()
table = Excel.add_sheet('Sheet1', cell_overwrite_ok=True)
for i in range(len(refer)):
    table.write(i, 0, '['+refer[i])
Excel.save(r'reference.xls')
