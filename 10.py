# 18.  Вивести номер п'ятого негативного елемента

from library import f3

arr = [f3(i) for i in range(1, 8)]
print("Масив:", arr)

negative_arr = [i for i in arr if i <= 0]
if len(negative_arr) < 5:
    print("Масив не має п'яти негативних елементів")
else:
    print("Номер п'ятого негативного елемента =", arr.index(negative_arr[4])+1)
