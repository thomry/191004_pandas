import openpyxl

wb    = openpyxl.load_workbook("produceSales.xlsx")
sheet = wb['Sheet']

PRICE_UPDATE = {'Garlic':3.07,
                'Celery':1.19,
                'Lemon' :1.27}
"""
for rowNum in range(2, sheet.max_rox + 1):
    produceName = sheet.call(row=rowNum, column = 1).value
    if produceName in PRICE_UPDATE:
        sheet.cell(row=rowNum, column = 2).value = PRICE_UPDATE[produceName]
"""
wb.save('update_produceSales.xlsx')

#if produceName == 'Garlic' :
#    cell0bj = 3.01
#if produceName == "Celery" :
#    cell0bj = 1.19
#if produceName == "Lemon"  :
#    cell0bj = 1.27

from openpyxl.styles import fonts, styleable
import style


font0bj1 = fonts.Font(name = 'Times New Roman', bold=True)
