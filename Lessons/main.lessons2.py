'''lst = [2, 3, 5]
def func(lst):
    a = lst[-3]
    del lst[-3]
    return a

print(func(lst))
print(lst)
'''
'''from random import randint

def randint(a, b):
    c = a - b
    ####
    return c

a = randint(1, 5)
print(a)'''


def add(a, b):
    c = a + b
    return c


d = add(4, 6)
print(d)


lst = [4, 7, 8, 9, -3, -6, -5,-2]
lst1 = [6, -8, -9, 4, 0, -1, -5]


def abs(l):
    l1 = []
    for item in l:
        if item < 0:
            itrm = -item
        l1.append(item)
    return l1
print(abs(lst), abs(lst1))

questions = ["Столица Франции?", "В каком году началсь Вторая Мировая война?", "Столица Австралии?"]
answers = ["париж", "1939", "канберра"]
user_score = 0

def set_questions(i):
    return f"Вопрос №{i + 1}: {questions[i]}"

def set_answer(i, user_answer):
    global user_score
    if user_answer.lower() == answers[i]:
        user_score += 1
        return "Правильно!"
    return f"Неправильно! Правильный ответ: {answers[i].title()}"

for i in range(len(questions)):
    print(set_questions(i))
    print(set_answer(i, input()))
print(f"Вы набрали {user_score} очков из {len(questions)}")

character = {'выносливость': 0,
             'здоровье': 0,
             'защита': 0}


def func(key):
    global character
    while True:
        value = int(input(f"Введите характеристику {key}: "))
        if 0 < value <= 100:
            break
        print("Не корректный ввод!")
    character[key] = value


for key in character.keys():
    func(key)


print(character)
improv = input("Улучшить характеристику бонусными фрагментами?")
if improv == "да":
    improv.title()
    for key, value in character.items():
        character[key] += 17
    print(character)
else:
    a = int(input("Ввести характеристику вручную?"))
    while True:
        if a == "да":
            for key, value in character.items():
                character[key] += input()
                if 0 < a <= 15:
                    print("Не корректный ввод!")
        else:
            print("Все остается без изменений")
        print(character)