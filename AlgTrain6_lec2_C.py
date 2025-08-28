'''
Домашнее задание для Лекции 2.
Задача C. Город Че.
'''

n, r = map(int, input().split())

distances = [int(dist) for dist in input().split()]

left, right = 0, 1
count = 0
while left < len(distances) and right < len(distances):
    while right < len(distances) and distances[right] - distances[left] <= r:
        right += 1
    count += len(distances) - right
    left += 1

print(count)