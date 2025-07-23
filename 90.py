'''
90. Стильная одежда
Difficulty: Intermediate
'''
import sys


N = int(input())
shirts = list(map(int, input().split()))

M = int(input())
pants = list(map(int, input().split()))

i1, i2 = 0, 0
dist = sys.maxsize
answer = []
while i1 < N and i2 < M:
    currDist = abs(shirts[i1] - pants[i2])
    if currDist  < dist:
        dist = currDist
        answer = [shirts[i1], pants[i2]]
    if shirts[i1] > pants[i2]: i2 += 1
    else: i1 += 1

print(' '.join(map(str, answer)))