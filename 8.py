# 18. Обчислити модуль добутку максимального і мінімального значень функції y.

from library import f1

i = 0
step = 1.8
arr_y = []

print("  x  |  y  \n--------------")
while i <= 18:
    y = round(f1(i), 2)
    arr_y.append(y)
    if i == 0:
        print("  0  | ", y)
    elif i != 0 and i < 10:
        print(i, " | ", y)
    else:
        print(i, "| ", y)
    i = round(i+step, 1)
print("--------------")

print("Модуль добутку максимального і мінімального значень функції y:",
      round(abs(max(arr_y)*min(arr_y)), 2))
