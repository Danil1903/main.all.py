import datetime
import json

PATH = "tasks.json"


def save_json(path, task):
    tasks = load_json(path)
    tasks.append(tasks)
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(tasks, file, ensure_ascii=False)


def load_json(path):
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def set_task(text, time):
    task = {"text": text, "time": time}


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
        save_json(PATH, set_task(text, time))
        print("Задача добавлена!")
    elif user_input == 2:
        tasks = load_json(PATH)
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]['text']}\n"
                  f"{tasks[i]['time']}")


if __name__ == "__main__":
    main()



key = input("ключ поиска: ")
s = []
for post in a:
    if key in post["text"]:
        s.append(post)
print(s)