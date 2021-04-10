import jieba  # 分词库
import matplotlib.pyplot as plt
from openpyxl import Workbook
import xlwt
import xlrd
from xlutils.copy import copy
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
def wc():
    txt = open("file2.txt", "r", encoding="utf-8").read()  # 读取数据
    words = jieba.lcut(txt)  # 分词
    counts = {}  # 词频统计
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())  # 结果显示
    items.sort(key=lambda x: x[1], reverse=True)

    wb = Workbook()
    sheet = wb.active
    sheet.append(['words', 'frequency'])

    for i in range(465):
        try:
            word, count = items[i]
            print("{0:<10}{1:>5}".format(word, count))
            words = word
            frequency = count
            sheet.append([words, frequency])
        except:
            print('第{0}条数据处理错误'.format(i))
    wb.save('bilibili_frequencydata.xlsx')
    label = list(map(lambda x: x[0], items[:30]))
    value = list(map(lambda y: y[1], items[:30]))
    plt.barh(range(len(value)), value, tick_label=label)
    plt.tight_layout()
    plt.savefig("temp.png", dpi=1000, bbox_inches='tight')
    plt.show()
