'''with open("file.txt", "a") as file:
    file.write("")'''

import json

users = [
    {
        "name": "Саша",
        "score": 45
    },
    {
        "name": "Виктор",
        "score": 3
    }
]

with open("file.json", "r") as file:
    data = json.load(file)
    print(data)

data.append({"name": "Евгений", "score": 12})

with open("file.json", "w") as file:
    json.dump(data, file)

with open("file.json", "r") as file:
    data = json.load(file)
    print(data)


def charc(user):
    with open("file.json", "r") as file:
        data = json.load(file)
    data.append(user)
    with open("file.json", "w") as file:
        json.dump(data, file)


for user in users:
    print(f"{user['name']} набрал {user['score']} очков!")

import json

user = {"name": "", "score": 0}


def get_questions(path="questions.json"):
    with open(path, "r") as file:
        questions = json.load(file)
    return questions


def set_question(question):
    return f"Вопрос: {question['question']}?" \
           f"Сложность: {question['difficulty']}/5"


def check_answer(question, user_answer):
    if user_answer.lower() == question['answer'].lower():
        user["score"] += question['difficulty']
        return f"Правильно!"
    return f"Неправильно, правильный ответ: {question['answer']},"


def get_users(users):
    with open("user.json", "r") as file:
        return json.load(file)


def save_user(users):
    users = get_users(users)
    users.append(users)
    with open("user.json", "w") as file:
        json.dump(user, file)


def print_statistics():
    users = get_users(user)
    for users in users:
        print(f"{user['name']} набрал {user['score']} очков")


def main():
    user["name"] = input("Введите свое имя: ")
    questions = get_questions()
    for question in questions:
        print(set_question(question))
        print(check_answer(question, input("Ответ:")))
    save_user(user)
    if input("Показать таблицу лидеров? ").lower() == "да":
        print_statistics()


if __name__ == "__main__":
    main()
