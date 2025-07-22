'''
144. Великое Лайландское переселение
Difficulty: Easy

stack
'''

N = int(input())
price = list(map(int, input().split()))

stack = []
result = [-1]*N
for i in range(N - 1, -1, -1):
    while stack and price[stack[-1]] >= price[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(i)

print(' '.join(map(str, result)))        