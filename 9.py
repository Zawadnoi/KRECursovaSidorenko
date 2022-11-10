# 18.  Обчислити суму збитків фірми. Чи мала фірма нульовий доход?

from library import f2

total = []
print("  Рік |  Статус  |  Доход  \n----------------------------")
for i in range(1991, 2002):
    y = round(100*f2(i), 2)
    total.append(y)
    if y > 0:
        print("", i, "| Прибуток | ", y)
    else:
        print("", i, "|  Збиток  | ", y)
print("----------------------------")


print("Сума збитків фірми =", abs(sum([x for x in total if x < 0])))
if 0 in total:
    print("Фірма мала нульовий дохід")
else:
    print("Фірма не мала нульового доходу")
