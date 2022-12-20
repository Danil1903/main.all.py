'''#первое задание
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
itog = 1
for _ in range(y):
    itog *= x
print(itog)

#второе задание
l = list(range(100, 1000))
l1 = []
for i in l:
    for j in str(i):
        if str(i).count(j) > 1:
            l1.append(i)
            break
print(l1)
print(len(l1))

l = list(range(100, 1000))
l1 = []
for i in l:
    i1 = str(i)
    for j in range(len(i1)):
        if i1[j] in i1[:j] or i1[j] in i1[j+1:]:
            l1.append(i)
            break
print(l1)
print(len(l1))

l = list(range(100, 9999))

l1 = []
for i in l:
    k = True
    i1 = str(i)
    for j in range(len(i1)):
        if i1[j] in i1[:j] or i1[j] in i1[j+1:]:
            k = False
            break
    if k:
        l1.append(i)

print(l1)
print(len(l1))

a = input(list())
while True:
    try:
        del a[a.index("3")]
    except:
        break
while True:
    try:
        del a[a.index("6")]
    except:
        break
print("", join(a))
'''
a = int(input())
b = int(input())
c = list(range(a, b+1))
d = []
for item in c:
    k = True
    for i in range(2, item):
        if item % i == 0:
            k = False
            break
    if k:
        d.append(item)
print(d)