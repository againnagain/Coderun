'''
Домашнее задание для Лекции 1.
Задача A. Плот.
'''

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x < x1:
    if y < y1:
        print("SW")
    elif y > y2:
        print("NW")
    else:
        print("W")
elif x > x2:
    if y < y1:
        print("SE")
    elif y > y2:
        print("NE")
    else:
        print("E")
else:
    if y < y1:
        print("S")
    elif y > y2:
        print("N")