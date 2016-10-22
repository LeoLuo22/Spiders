import xlrd

file = xlrd.open_workbook("F://stu_num.xls")
table = file.sheet_by_index(0)
count = 0
for value in table.col_values(4):
    value += "\n"
    count += 1
    with open("stu_num.txt", "a") as fh:
        fh.write(value)
print(count)
