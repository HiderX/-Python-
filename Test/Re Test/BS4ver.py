import requests
import xlwt
import xlrd
from bs4 import BeautifulSoup
from xlutils.copy import copy


def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")

def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()


url = 'https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

wrapList = []
i =1
for a in soup.find_all('a', class_="title",target='_blank'):
    print('\n','title is ',a.get_text(),'link is ',a.get('href','default'))
    item = []
    item.append(i) # add  id
    item.append(a.get_text())   # add  text
    itemUrl = a.get('href','default')
    iSoup = BeautifulSoup( requests.get(itemUrl).text, 'lxml')
    j =1
    i = i + 1
    itemTag = ''
    for tag in iSoup.find_all('a', target='_blank'):
        itemTag = itemTag + tag.get_text() + '  ,'
        # item.append( tag.get_text())
        j = j+1
    print('\n',"tag is" , itemTag )
    item.append(a.get('href','default'))# add link
    item.append(itemTag)  # add  itemTag
    wrapList.append(item)

print('*'*100)


book_name_xls = 'B站数据分析工作簿.xls'

sheet_name_xls = '排行榜'

value_title = [["id", "标题",  "链接","标签"], ]

write_excel_xls(book_name_xls, sheet_name_xls, value_title)
write_excel_xls_append(book_name_xls, wrapList)

