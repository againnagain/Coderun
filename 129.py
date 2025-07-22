'''
129. Родословная: подсчет уровней
Difficulty: Easy

tree, depth-first search (dfs), dictionary
'''

def get_depth(node):
    if node in depth:
        return depth[node]
    
    d = get_depth(family_tree[node]) + 1
    depth[node] = d
    return d


family_tree = dict()
family = set()

for pair in range(int(input())-1):
    child, parent = input().split()

    family_tree[child] = parent

    family.add(child)
    family.add(parent)

ancestor = (family - family_tree.keys()).pop()

depth = {ancestor : 0}
for child in sorted(list(family_tree.keys()) + [ancestor]):
    if child not in depth:
        get_depth(child)
    print(f'{child} {depth[child]}')