'''from turtle import * #мы добавляем конструкцию turtle
color ("black", "red")# какими цветами что будет рисоваться
m = 100 # диопазон действия (всегда одно и тоже)
begin_fill()# спипок
left(90)# сюда пишем градус (он всегда один вроде как ,но всё равно смотри
for i in range (4): # сюда пишем значение ,которое у нас требуют в задании ,в основном всегда пишем значение 3 ,но если больше 4 ,то пишем которое у нас в задании .это если что где написанно ПОВТОРИ 6
    forward(10*m)# здесь пишем что у нас в задании ,в задании у нас вперёд 10 ,m- этл у нас диапозон действия
    right(90)# тоже самое что и сверху ,только вправо
end_fill()#завершаем список
canvas = getcanvas()#октрываем новый
cnt = 0
for y in range(-90*m, 90*m, m):#здесь перебираем ,значения в скобках менятся от того ,что у нас просят в строке right
    for x in range(-90 * m, 90 * m, m):#тоже самое ,что и выше
        item = canvas.find_overlapping(x, y, x, y)#всегда пишем это
        if len(item) == 1 and item[0] == 5:# тоже не изменимо
            cnt += 1
print(cnt)
done()
exit()
'''

def f(x, h):
    if h == 3 and x >= 63:
        return 1
    elif h == 3 and x < 63:
        return 0
    elif x >= 63 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия победителя
        else:
             return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия проигравшего(неудачный ход)

for x in range(1, 63):
    if f(x, 1) == 1:
        print("Задача 19: ", x)
        break


def f(x, h):
    if h == 3 and x >= 54:
        return 1
    elif h == 3 and x < 54:
        return 0
    elif x >= 54 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 3, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 3, h + 1)


for x in range(1, 54):
    if f(x, 1) == 1:
        print(x)
        break



def f(x, h):
    if (h == 3 or h == 5) and x >= 68:
        return 1
    elif h == 5 and x < 68:
        return 0
    elif x >= 68 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)

def f1(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0
    elif x >= 68 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x + 4, h + 1) or f1(x * 5, h + 1)
        else:
            return f1(x + 1, h + 1) and f1(x + 4, h + 1) and f1(x * 5, h + 1)

for x in range(1, 68):
    if f(x, 1) == 1:
        print(x)
print("====")
for x in range(1, 68):
    if f1(x, 1) == 1:
        print(x)