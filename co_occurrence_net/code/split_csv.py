import csv
import pandas as pd
import xlsxwriter

# 创建工作簿
workbook = xlsxwriter.Workbook('NIH共现分析数据.xlsx')  # 创建一个excel文件
# 创建工作表
worksheet = workbook.add_worksheet('Sheet1')  # 在文件中创建一个名为这是sheet1的sheet,不加名字默认为sheet1


file = pd.read_excel(r"C:\Users\Administrator\PycharmProjects\python_gephi\Data Science-Machine Learning and Artificial Intelligence共现分析数据.xlsx",sheet_name='Sheet1')
locs = file.shape[0]
print(locs)
c = 0
d = 0
for i in range(0,locs):
    loc = list(file.loc[i])
    # 写入数据
    terms = loc[0]
    terms_list = terms.split(";")
    project_number = loc[1]
    print(terms_list)
    print(project_number)
    for term in terms_list:
        worksheet.write(c, 0, term)  #
        worksheet.write(c, 1, project_number)
        c += 1


workbook.close()