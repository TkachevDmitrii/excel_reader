import openpyxl
import matplotlib.pyplot as plt
from collections import Counter


# Забьем массив проданных фильмов в 1 и 2 магазине (по отдельности)
def parse(wb):
    sheet = wb['sells']
    buyer_val_shop_1 = []
    buyer_val_shop_2 = []
    for v in sheet['A2:E14597']:
        if v[4].value == 'Магазин 1':
            buyer_val_shop_1.append(v[2].value)
        else:
            buyer_val_shop_2.append(v[2].value)
    return buyer_val_shop_1, buyer_val_shop_2


# Ф-ция для создания дикта
def dict_of(x, y, z):
    for i in x:
        a = y.count(i)
        z.setdefault(i, a)
    return z


# ТОП-5
def count_top(x):
    k = Counter(x)
    high = k.most_common(5)
    a = []
    b = []
    for i in high:
        a.append(i[0])
        b.append(i[1])
    return a, b
