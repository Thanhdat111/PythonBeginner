import openpyxl as xl

print(xl.__version__)
# access to file excel
wb = xl.load_workbook('transactions.xlsx')
#
# access to sheet
sheet = wb['Sheet1']
# access to cell have two way
cell = sheet['a1']

#delete colums
sheet.delete_cols(1, 3)
# access all cell
# change range 1-2 to ignore row 1(name,price,...)
for row in range(2, sheet.max_row + 1):
    # access to cell column 3
    cell = sheet.cell(row, 3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row, 4)
    corrected_price_cell.value = corrected_price

wb.save('transactions2.xlsx')
#wb.save('transactions2.xlsx')
