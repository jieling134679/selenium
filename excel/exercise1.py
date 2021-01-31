import xlrd

#返回一个Book类型的对象，execl的信息就存储在Book对象中
book = xlrd.open_workbook("income.xlsx")

print("包含表单数量 " + str(book.nsheets))
print(book.sheet_names())

sheet = book.sheet_by_index(0)
sheet = book.sheet_by_name('2018')

print(sheet.nrows)
print(sheet.name)
print(sheet.number)
print(sheet.ncols)

print(sheet.cell_value(1, 1))

print(sheet.row_values(10))
print(sheet.col_values(0))#第一列
print(sheet.col_values(0, 3, 4))

list = sheet.col_values(0)
for a, b in enumerate(list):
    print(str(a))
    print(str(b))
