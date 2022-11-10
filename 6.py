# 18) z = |x-y|;

from library import f23, f24


x = 0
y = 1
for k in range(1, 24):
    x += f23(k)
    y *= f24(k)

z = abs(x-y)

print("z = |x-y| =", z)
