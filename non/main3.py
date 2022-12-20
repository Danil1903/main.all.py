from random import randint
user_score = 0
while True:
    print("Угадайте число от 1 до 10, или напишите выход")
    user_input = input().lower()
    if user_input in ("выход", "exit", "quit"):
        print("Программа завершает выполнение...")
        break
    user_input = int(user_input)
    rand_int = randint(1, 11)
    if user_input == rand_int:
        user_score +=1
        print(f"Вы угадали, ваш счет {user_score}")
    else:
        print(f"Вы не угадали, было загадано число {rand_int}")
