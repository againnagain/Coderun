A = int(input())
B = int(input())
C = int(input())
D = int(input())
    
candidates = list() # candidates (M, N)

if A > 0 and C > 0:
    candidates.append(
        (B + 1, D + 1)
    )

if B > 0 and D > 0:
    candidates.append(
        (A + 1, C + 1)
    )

if A > 0 and B > 0:
    candidates.append(
        (max(A, B) + 1, 1)
    )

if C > 0 and D > 0:
    candidates.append(
        (1 , max(C, D) + 1)
    )

min_sum = float('inf')
best = None
for M, N in candidates:
    curr_sum = M + N
    if curr_sum < min_sum:
        min_sum = curr_sum
        best = (M, N)

print(' '.join(map(str, best)))