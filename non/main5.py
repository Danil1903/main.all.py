# первое задание
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for item in range(a, b):
    if item % 7 == 0:
        print(item, end=" ") #не понимаю работает ли

# второе задание
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for item in range(a, b):
    print(item, end=" ")
for item in range(b - 1, a - 1, -1):
    print(item, end=" ")
for item in range(a, b):
    if item % 7 == 0:
        print(item, end=" ")
for item in range(a, b):
    if item % 5 == 0:
        print(item, end=" ")

# третье задание
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

for item in range(a, b + 1):
    if item % 3 != 0 and item % 5 != 0:
        print(item)
    if item % 3 == 0 and item % 5 == 0:
        print("Fizz Buzz")
    else:
        if item % 3 == 0:
            print("Fizz")
        if item % 5 == 0:
            print("Buzz")  # вот это уже не сам сделал
