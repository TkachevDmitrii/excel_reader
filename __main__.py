import openpyxl
from openpyxl import Workbook
from utils import ExcelReader
from utils import PieChart

# Загрузим xlsx - файл
wb = openpyxl.load_workbook("./file/sales.xlsx")

# Проданные фильмы в 1 и 2 магазинах
buyer_val_shop_1, buyer_val_shop_2 = ExcelReader.parse(wb)

# Удаление дубликатов фильмов в 1 и 2 магазинах
dup_del_shop_1 = list(set(buyer_val_shop_1))
dup_del_shop_2 = list(set(buyer_val_shop_2))


top_5_shop_1 = {}
top_5_shop_2 = {}

# Словарь {фильм : кол-во проданных копий}
top_5_shop_1 = ExcelReader.dict_of(dup_del_shop_1, buyer_val_shop_1, top_5_shop_1)
top_5_shop_2 = ExcelReader.dict_of(dup_del_shop_2, buyer_val_shop_2, top_5_shop_2)

# Топ - 5 фильмов в каждом магазине
top_5_shop_1 = ExcelReader.count_top(top_5_shop_1)
top_5_shop_2 = ExcelReader.count_top(top_5_shop_2)

# Массив фильмов ТОП-5
movies_shop_1 = top_5_shop_1[0]
movies_shop_2 = top_5_shop_2[0]

# Массив проданных копий ТОП-5
number_of_copy_shop_1 = top_5_shop_1[1]
number_of_copy_shop_2 = top_5_shop_2[1]

# Построение pie-chart
PieChart.build(movies_shop_1, number_of_copy_shop_1)
PieChart.build(movies_shop_2, number_of_copy_shop_2)