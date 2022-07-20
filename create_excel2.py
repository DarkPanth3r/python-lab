# import xlsxwriter module
import xlsxwriter
 
workbook = xlsxwriter.Workbook('Test_excel.xlsx')
worksheet1 = workbook.add_worksheet('Folha1.xlsx')
worksheet2 = workbook.add_worksheet('Folha2.xlsx')
 
# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0
 
content = ["ankit", "rahul", "priya", "harshita",
                    "sumit", "neeraj", "shivam"]
 
# iterating through content list
for item in content :
 
    # write operation perform
    worksheet1.write(row, column, item)
 
    # incrementing the value of row by one
    # with each iterations.
    row += 1

row = 0
column = 0

content2 = ["chupa", "aqui", "clementina", "ahahah",
                    "Vais ver que", "Melhor", "não ha"]    
for item in content2 :
 
    # write operation perform
    worksheet2.write(row, column, item)
 
    # incrementing the value of row by one
    # with each iterations.
    column += 1
     
workbook.close()
