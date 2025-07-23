'''
52. Словарь синонимов
Difficulty: Easy
'''

syn1 = dict()
syn2 = dict()

for pair in range(int(input())):
    word1, word2 = input().split()
    syn1.update({word1 : word2})
    syn2.update({word2 : word1})

inWord = input()
print(syn1[inWord]) if syn1.get(inWord) != None else print(syn2[inWord])