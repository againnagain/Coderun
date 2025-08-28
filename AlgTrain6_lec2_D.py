'''
Домашнее задание для Лекции 2.
Задача D. Лучший отдых.
'''

n, k = map(int, input().split())
tasks = [int(a_i) for a_i in input().split()]
tasks.sort()

left, right = 0, 0
ans = 0
while left < len(tasks) and right < len(tasks):
    if tasks[right] - tasks[left] <= k:
        ans = max(ans, right - left + 1)
        right += 1
    else:
        left += 1

print(ans)