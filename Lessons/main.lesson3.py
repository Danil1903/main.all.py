from random import shuffle

questions = [{"question": "Сколько сторон у треугольника",
              "difficulty": 1,
              "answer": "3"},
             {"question": "Какой цвет фенолофталин в щелочной среде",
              "difficulty": 5,
              "answer": "малиновый"},
             {"question": "Кто такой Святослав Рихтер",
              "difficulty": 4,
              "answer": "пианист"},
             {"question": "первый человек в космосе (фамилия)",
              "difficulty": 2,
              "answer": "Гагарин"},
             {"question": "Сколько планет в Солнечной системе",
              "difficulty": 3,
              "answer": "8"}]
users = []


def srart_game():
    user = dict(name='',
                score=0)
    user["name"] = input("Введите свое имя: ")
    return user


def statistick(user):
    for users1 in user:
        if users1(user, input()):
            print(users1)


def set_question(question, i):
    return f'Вопрос №{i}: {question["question"]}?' \
           f'Сложность {question["difficulty"]}/5'


def check_answer(question, user_answer):
    return user_answer == question["answer"]


def main():
    while True:
        user = srart_game()
        i = 1
        shuffle(questions)
        for question in questions:
            print(set_question(question, i))
            if check_answer(question, input("Ответ: ")):
                print("Правильно! Молодец!")
                user["score"] += question["difficulty"]
            else:
                print(f'Неправильно, правильный ответ: {question["answer"]}')
            i += 1
        print(f'{user["name"]}, вы набрали {user["score"]} очков!')
        users.append(user)
        while True:
            print("Чтобы выйти, напишите 1\n"
                  "Чтобы начать заново, напишите 2\n"
                  "Чтобы посмотреть статистику, напишите 3\n"
                  "Чтобы посмотреть статистику предыдущих участников, напишите 4")
            user_input = input()
            if user_input == "1":
                exit()
            elif user_input == "2":
                break
            elif user_input == "3":
                print(users)
            elif user_input == "4":
                print(users)


if __name__ == "__main__":
    main()