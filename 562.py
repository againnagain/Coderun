'''
562. 1984
Difficulty: Easy
'''


n, m = map(int, input().split())

stop_words = [input() for word in range(n)]
messages = [input() for message in range(m)]

flag = True
for message in messages:
    for stop_word in stop_words:
        if stop_word in message:
            print('DELETE')
            flag = False
            break
    if flag == True:
        print('KEEP')
    flag = True