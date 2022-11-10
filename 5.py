# 18. 1 фингер =11.4 см = 4.5 дюймів;

strings = int(input("Кількість строк = "))
step = int(input("Шаг = "))

print("\nФингер  |   См   |  Дюйм\n----------------------------")

for i in range(1, strings*step, step):
    if i < 10:
        print("    ", i, " | ", round(i*11.4, 2), " | ", round(i*4.5, 2))
    else:
        print("   ", i, " | ", round(i*11.4, 2), "|  ", round(i*4.5, 2))
