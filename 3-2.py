from library import f20, f21, f22
work_types = {"А": 0.1, "Б": 0.15, "В": 0.2}

work = input("Тип роботи =")

if work == "А":
    money = 100*abs(f20(18)+50)
elif work == "Б":
    money = 150*abs(f21(18)+100)
elif work == "В":
    money = 200*abs(f22(18)+135)

tax = money * work_types[work]
for_issue = money-tax

print("Нарахована сума =", round(money, 2))
print("Податок =", round(tax, 2))
print("До видачі =", round(for_issue, 2))
