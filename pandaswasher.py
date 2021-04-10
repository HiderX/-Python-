import pandas as pd


def washer():
    df = pd.read_excel('bilibili_tag.xls')
    df2 = df['标签'].str.split(',', expand=True)
    print(df2)
    df2.to_excel('excel_to_python.xlsx', sheet_name='排行榜',header=None,index=False)
    print('开始写入txt文件...')
    df2.to_csv('file2.txt', header=None, sep=' ', index=False)  # 写入，逗号分隔
    print('文件写入成功!')
