# первое задание
a = int(input())
for i in range(2, a + 1):
    k = True
    for f in range(2, i):
        if i % f == 0:
            k = False
            break
    if k:
        print(i, end=' ')

# второе и третье задание
numbers = [int(i) for i in input().split(' ')] #я это нашел в интеренете, на много проще с этим
for i in numbers:
    for item in range(1, 11):
        print(f'{i}*{item}={i * item}')


