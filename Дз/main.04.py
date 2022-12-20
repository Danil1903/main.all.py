#первое задание
a = input()
l = len(a)
l = l//2
for i in range(l):
    if a[i] != a[-1-i]:
        print("Это не палиндром")
        quit()
print("Это палиндром")
#третье задание
file = open('text.txt')

words = 0

for line in file:
    words += len(line.split())

print("Всего слов:", words)
