'''a = (5, 8, 9, 3, 23, 45)
b = (8, 4, 6, 2, 7, 3)
c = []
for i in a:
    if i in a:
        continue
    c.append(i)

for i in b:
    if i in a:
        continue
    c.append(i)
print(c)'''

'''a = [[5, 8, 9, 3, 23, 45],
     [8, 4, 6, 2, 7, 3],
     [4, 8, 16, 3, 5, 23]]
b = []
for i in range(len(a)):
    c = a[:]
    del c[i]
    d = []
    for item in c:
         d.extend(item)
    for item in a[i]:
        if i in d:
            continue
        b.append(item)
print(b)'''

a = [0, 1]

while True:
    if (s := a[-1] + a[-2]) > 100:
        break
    a.append(s)
print(a)

a = [0, 1]
answer = ("Да", "Yes")
if user_answer := input() in answer:
    print("Ok")
else:
    print("неок")


