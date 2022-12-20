'''def f(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return f(n - 1) + 2 * f(n - 2)
print(f(4))


import turtle as t
k = 40
t.left(90)
t.speed(10)
for i in range(8):
    t.forward(6 * k)
    t.right(120)
t.up()
t.speed(10)m
for x in range(-1, 7):
    for y in range(-1, 8):
        t.goto(x * k, y * k)
        t.dot(5)
t.done()

'''

def f(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    if n > 2:
        return f(n - 2) + f(n - 1)
print(f(10))