a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b:
    for i in range(a - 1, b, -1):
        print(i)
else:
    print("Числа a и b одинаковы.")
