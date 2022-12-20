import datetime
import json

PATH = "json.2file"

users = [
    {
        "name" : input("Введите свой ник: "),
        "date" : input("Введите дату: "),
        "text" : input("Введите текст: ")}
]


def save_json(path, posts):
    posts = load_json(path)
    posts.append(posts)
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(posts, file, ensure_ascii=False)


def load_json(path):
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def set_posts(text, time):
    posts = {"text": text, "time": time}


def main():
    print("0. Выход.\n"
          "1. Добавить задачу.\n"
          "2. Вывести список задач.\n")
    user_input = int(input())
    if user_input == 0:
        quit()
    elif user_input == 1:
        print("Введите текст задачи:")
        text = input()
        time = str(datetime.datetime.now()).split(".")[0]
        save_json(PATH, set_posts(text, time))
        print("Задача добавлена!")
    elif user_input == 2:
        posts = load_json(PATH)
        for i in range(len(posts)):
            print(f"{i + 1}. {posts[i]}\n"
                  f"{posts[i]}")


key = input("Ключ поиска: ")
s = []
for post in users:
    if key in post["text"]:
        s.append(post)
print(s)


if __name__ == "__main__":
    main()