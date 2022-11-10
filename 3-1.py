from library import f20, f21
from math import tan, log, exp


x = int(input("x = "))
a = int(input("a = "))
b = int(input("b = "))

c = int(input("c = "))
d = int(input("d = "))

# А
if abs(x) < 10:
    y = f20(tan(x+a)-log(abs(b+7), 18))
if abs(x) >= 10:
    y = f21(c*(x**2+d*exp(1.3))**0.2)

# Б
# y = f20(tan(x+a)-log(abs(b+7), 18)
#         ) if abs(x) < 10 else f21(c*(x**2+d*exp(1.3))**0.2)

print("y =", y)
