f = input('Из какой единицы: ')
t = input('В какую единицу: ')
v = float(input('Значение: '))
if f == "км": m = v * 1000
elif f == "м": m = v
elif f == "см": m = v / 100
elif f == "мм": m = v / 1000
elif f == "mi": m = v * 1609.34
else: m = v * 0.9144   # yd
if t == "км": r = m / 1000
elif t == "м": r = m
elif t == "см": r = m * 100
elif t == "мм": r = m * 1000
elif t == "mi": r = m / 1609.34
else: r = m / 0.9144   # yd
print(round(r, 4))
