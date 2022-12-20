'''#первое задание
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
numb = 0
numb1 = 0
numb2 = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        numb += i
        print(f"Сумма нечетных: {numb}")
    if i % 2 == 0:
        numb1 += i
        print(f"Сумма четных: {numb1}")
    if i % 9 == 0:
        numb2 += i
        print(f"Сумма кратных на 9: {numb2}")'''

#второе задание
a = int(input("Введите длину строки: "))
b = input("Введите символ: ")
for i in range(a):
        print(b)



#третье задние
while True:
    a = int(input())
    if a > 0:
        print("Number is positive")
    elif a < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
    if a == 7:
        print("Good bye!")
        exit()

#четвертое задание
a = []
while True:
    numb = int(input())
    a.append(numb)
    if numb == 7:
        print(f"Сумма чисел, {sum(a)}")
        print(f"Максимальное число, {max(a)}")
        print(f"Минимальное число, {min(a)}")
        exit()