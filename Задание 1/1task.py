a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Площадь: {s:.2f}")
else:
    print("Такого треугольника не существует")
