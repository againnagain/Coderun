'''
Домашнее задание для Лекции 2.
Задача A. Префиксные суммы.
'''

n = int(input())
a = [int(a_i) for a_i in input().split()]

prefixSum_a = [0 for i in range(n)]
prefixSum_a[0] = a[0]

for i in range(1, len(a)):
    prefixSum_a[i] = prefixSum_a[i-1] + a[i]

print(' '.join(map(str, prefixSum_a)))