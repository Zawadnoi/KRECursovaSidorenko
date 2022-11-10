from library import f25


def e_comparison(x: float) -> bool:
    if int(x) != x:
        buf = str(x).split('.')
        if len(buf[1]) >= 3:
            return True
    return False


k = 1               # Крок послідовності
ak = [f25(k)/k]     # Послідовність (у вигляді масива)

while True:
    k += 1
    ak.append(f25(k)/k)
    q = ak[-2]/ak[-1]
    summa = ak[-1]/(1-q)
    if e_comparison(summa):
        break

print("Сума спадної послідовності =", summa)
print("Кількість елементів послідовності:", k)
