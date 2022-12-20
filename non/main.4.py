'''a = int(input("Введите число начала диапазона: "))
b = int(input("Введите число конец диапазона: "))

l1 = []
l2 = []
l3 = []

for item in range(a, b + 1):
    if item % 2:
        l2.append(item)
    else:
        l1.append(item)
    if not item % 2:
        l3.append(item)
sum1 = sum(l1)
sum2 = sum(l2)
sum3 = sum(l3)

avg1 = sum1 / len(l1)
avg2 = sum2 / len(l2)
avg3 = sum3 / len(l3)

print(f"Сумма четных чисел: {sum1}, среднее: {avg1}\n"
      f"Сумма нечетных чисел: {sum2}, среднее: {avg2}\n"
      f"Сумма чисел кратных 9: {sum3}, среднее: {avg3}\n")


num = int(input("Введите число: "))
char = input("Введите символ: ")
for _ in range(num):
    print(char[0])'''

print("Для выхода введите 7")
l = []
while True:
    user_input = int(input("Введите число: "))
    if user_input == 7:
        break
    l.append(user_input)
print(f"Сумма чисел, {sum(l)}")
print(f"Максимальное число, {max(l)}")
print(f"Минимальное число, {min(l)}")
print("Good bye!")