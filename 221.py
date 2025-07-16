'''
221. Линейно разделимая выборка
Difficulty: Easy
'''


import math

EPOCHS = 10
LEARNING_RATE = 1
LAMBDA = 0.1

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

n, m = map(int, input().split())
objects = [list(map(float, input().split())) for _ in range(n)]
weights = [0.0 for _ in range(m)]
bias = 0.0

for epoch in range(EPOCHS):
    for obj in objects:
        x = obj[:-1]
        y = obj[-1] 

        y_pred = sum(w * xi for w, xi in zip(weights, x)) + bias

        grad_coeff = -y * sigmoid(-y * y_pred)
        
        for i in range(m):
            weights[i] -= LEARNING_RATE * (grad_coeff * x[i] + LAMBDA * weights[i])
        bias -= LEARNING_RATE * grad_coeff

print(' '.join(list(map(str, weights))))