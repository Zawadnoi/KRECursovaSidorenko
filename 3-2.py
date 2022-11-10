from library import f20, f21, f22

work = input("Тип роботи = ")

if work in ["А", "A","a", "а"]:
    money = 100*abs(f20(18)+50)
    percent = 0.1
elif work in ["Б", "б"]:
    money = 150*abs(f21(18)+100)
    percent = 0.15
elif work in ["В", "в"]:
    money = 200*abs(f22(18)+135)
    percent = 0.2
else:
    money = 0
    percent = 0

tax = money * percent
for_issue = money-tax

print("Тип роботи =", work)
print("Нарахована сума =", round(money, 2))
print("Податок =", round(tax, 2))
print("До видачі =", round(for_issue, 2))
