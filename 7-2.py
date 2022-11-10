from library import f25
from math import factorial


def e_comparison(x: float) -> bool:
    if int(x) != x:
        buf = str(x).split('.')
        if len(buf[1]) >= 3:
            return True
    return False


x = 0.3                                         # Довільне дане
k = 1                                           # Крок послідовності
# Послідовність (у вигляді масива)
ak = [(-1**k)*((f25(k)*x**k)/factorial(k))]

while k < 10:
    k += 1
    ak.append((-1**k)*((f25(k)*x**k)/factorial(k)))
    q = ak[-2]/ak[-1]
    summa = ak[-1]/(1-q)
    if e_comparison(summa):
        break

print("Сума спадної послідовності =", summa)
print("Кількість елементів послідовності:", k)
