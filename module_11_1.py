import matplotlib.pyplot as plt

# линейный график
# x = [1, 2, 6, 8]
# y = [3, 4, 7, 9]
# plt.plot(x, y, color="purple", marker="o", markersize=10)
# plt.xlabel("Ось x")
# plt.ylabel("Ось y")
# plt.title("график первый")
# plt.show()

# диаграмма рассеяния
# x = [3, 6, 20, 31]
# y = [24, 76, 60, 80]
# plt.scatter(x, y)
# plt.show()

# столбчатая диаграмма
# x = ["BNB", "ETH", "BCH", "SOL"]
# y = [582.16, 2_467, 353.23, 168.15]
#
# plt.bar(x, y, label="Цена")
# plt.xlabel("Название актива")
# plt.ylabel("Цена актива")
# plt.title("Столбчатая диаграмма криптовалюты")
# plt.legend()
# plt.show()

# круговая диаграмма
val = [25, 35, 12, 8, 20]
cars = ["Audi", "BMW", "Porsche", "Volkswagen", "Mercedes"]

plt.pie(val, labels=cars, autopct="%1.f%%")
plt.title("Распределение марок автомобилей в автосалоне")
plt.show()
