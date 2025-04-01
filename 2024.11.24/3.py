def tree_leaves(branches):
    count = 0
    for branch in branches:
        if isinstance(branch, list):
            count += tree_leaves(branch)
        elif branch == 'leaf':
            count += 1
    return count

#C:\Git\Sajgakova\2024.11.24>python -i 3.py
#>>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', '\leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'\], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
#>>> tree_leaves(tree)
#38