'''
570. Лента рекоммендаций
Difficulty: Easy
'''

p, n, k = map(int, input().split())

recommendations = [input() for _ in range(p)]
recommendations_ids = list(map(int, input().split()))

themes_count = {} 
selected = 0

for i in range(p):
    theme = recommendations[i]
    video_id = recommendations_ids[i]
    
    if theme not in themes_count:
        themes_count[theme] = 0
    
    if themes_count[theme] < k:
        print(f"{theme} #{video_id}")
        themes_count[theme] += 1
        selected += 1
    
    if selected == n:
        break