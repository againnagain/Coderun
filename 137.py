'''
137. Минимальный прямоугольник
Difficulty: Easy
'''

import sys

leftBottom = [sys.maxsize, sys.maxsize]
rightTop = [-sys.maxsize, -sys.maxsize]

for i in range(int(input())):
    xi, yi = map(int, input().split())

    leftBottom[0] = min(leftBottom[0], xi)
    leftBottom[1] = min(leftBottom[1], yi)

    rightTop[0] = max(rightTop[0], xi)
    rightTop[1] = max(rightTop[1], yi)

print(' '.join(map(str, leftBottom + rightTop)))