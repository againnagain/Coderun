'''
566. Пушистики
Difficulty: Easy
'''

N, t = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()

iter = 0
while t > 0:
    if iter <= N - 1:
        t -= cards[iter]
        if t >= 0:
            iter += 1
    else:
        break

print(iter)