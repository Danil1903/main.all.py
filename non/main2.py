x = float(input("Введите число: "))
oper = input("Введите степень: ")
if oper == "2":
    print(x**2)
if oper == "3":
    print(x**3)
if oper == "4":
    print(x**4)
if oper == "5":
    print(x**5)
if oper == "6":
    print(x**6)
if oper == "7":
    print(x**7)

# третье задание
a = input("Выбрать оператор мобильной связи?\n"
          "да/нет: ")
connect = a
if connect == "да":
    bill = 1
    tele = 2
    mega = 3
else:
    print("Закройте вкладку!")
    exit()

x = input(f"Билайн = {bill}\n"
          f"Теле2 = {tele}\n"
          f"Мегафон = {mega}\n")
balence = input(f"Баланс оператора {x}, 250руб #enter")
b = 250

spend = input(f"Узнать сколько рублей в минуту требуется в разных операторов? ")
if spend == "да":
    bill = 7
    tele = 8
    mega = 9
else:
    print("Ошибка, попробуйте снова")
    exit()

print(f"Билайн = {bill}\n"
      f"Теле2 = {tele}\n"
      f"Мегафон = {mega}\n")

print("Подсчет:\n"
      f"{250 - 7}\n"
      f"{250 - 8}\n"
      f"{250 - 9}\n")  # не смог по другому сделать

# четвертое задание
a = int(input("Введите продажи 1 менеджера: "))
b = int(input("Введите продажи 2 менеджера: "))
c = int(input("Введите продажи 3 менеджера: "))

premia = 200

if a > 1000:
    zp1 = premia + a * 0.08
else:
    if a < 500:
        zp1 = premia + a * 0.03
    else:
        zp1 = premia + a * 0.05
if b > 1000:
    zp2 = premia + b * 0.08
else:
    if b < 500:
        zp2 = premia + b * 0.03
    else:
        zp2 = premia + b * 0.05
if c > 1000:
    zp3 = premia + c * 0.08
else:
    if c < 500:
        zp3 = premia + c * 0.03
    else:
        zp3 = premia + c * 0.05
if zp1 > zp2 and zp1 > zp3:
    print("Лучший по продажам 1 менеджер!")
if zp2 > zp1 and zp2 > zp3:
    print("Лучший по продажам 2 менеджер!")
if zp3 > zp1 and zp3 > zp2:
    print("Лучший по продажам 3 менеджер!")

print(f"Зарплата 1 менеджера, {zp1}\n"
      f"Зарплата 2 менеджера, {zp2}\n"
      f"Зарплата 3 менеджера, {zp3}\n")