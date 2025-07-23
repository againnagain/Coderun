'''
57. Инопланетный геном
Difficulty: Intermediate
'''

def get_gen_bases(gen):
    bases = dict()
    for i in range(len(gen)-1):
        base = gen[i] + gen[i+1]
        bases[base] = bases[base] + 1 if bases.get(base) != None else 1

    return bases

gen1 = get_gen_bases(input())
gen2 = get_gen_bases(input())

result = 0
for base, count in gen1.items():
    if base in gen2:
        result += count

print(result)