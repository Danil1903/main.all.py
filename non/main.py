'''a = "text"
for i in a:
    print(i)

questions = ["3?", "6?", "7?", "12?"]
answers = [0, 0, 0, 0]
sp = [0, 0, 0, 0]
user_score = 0
for i in range(len(questions)):
    print(f"Вопрос: {questions[i]}")
    user_answer = int(input())
    if user_answer == answers[i]:
        print("Правильно")
        user_score += 1
    else:
        print("Неправильный")
print(f"")'''

'''questions = ["luck", "strength", "speed", "intellect"]
sp = [0, 0, 0, 0]
for i in range(len(questions)):
    while True:
        print(f"Укажите характеристику: {questions[i]}")
        user_input = int(input())
        if 0 <= user_input <= 10:
            sp[i] = user_input
            break
        print("Некорректный ввод")
print(sp)'''


'''words = ["ab..pt", "br..ht", "ca..ure", "d..ris", "ed..ate"]
insert = ["ru", "ig", "pt", "eb", "uc"]
user_score = 0
a = input("Привет, проверим твои знания английского языка\n"
          "Если готов, то вперед -----> да/нет\n")
if a == "да":
    print("Удачи")
else:
    print("Закройте программу")
    exit()

for i in range(len(words)):
    while True:
        print(f"Введите те буквы на месте точек которые будут правильные: {words[i]}")
        user_insert = input()
        if user_insert == insert[i]:
            print("Правильно")
            user_score += 5
            break
        print("Неверный ввод, попробуйте снова")
        user_score -= 1
print(f"Ты прошел мини-игру, твой счет {user_score}")'''

a = [3, 7, 9, 14, 28, 31]
b = []
for i in a:
    if i % 7 == 0:
        b.append(i)
print(b)

a = ["text", "kek", "lolik", "babushka"]
b = []
for i in a:
    i += str(len(i))
    b.append(i)
print(a)
print(b)

a = [3, 7, 10, 4]
b = []
for i in a:
    i *= i
    b.append(i)
print(b)

a = ["text", "kek", "lolik", "babushka"]
b = []
for i in a:
    if "e" in i:
        b.append(True)
    else:
        b.append(False)
print(b)