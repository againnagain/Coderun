'''
82. Кондиционер
Difficulty: Easy
'''

troom, tcond = map(int, input().split())
mode = input()

answer = None
match mode:
    case 'freeze':
        answer = tcond if troom > tcond else troom
    case 'heat':
        answer = tcond if troom < tcond else troom
    case 'auto':
        answer = tcond
    case 'fan':
        answer = troom
    
print(answer)
