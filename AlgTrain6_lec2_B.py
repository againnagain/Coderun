'''
Домашнее задание для Лекции 2.
Задача B. Сумма номеров.
'''

N, K = map(int, input().split())
numbers = [int(number) for number in input().split()]

count = 0
right = 0
currSum = 0

for left in range(len(numbers)):
    while right < len(numbers) and currSum < K:
        currSum += numbers[right]
        right += 1
    
    if currSum == K:
        count += 1
    
    currSum -= numbers[left]

print(count)