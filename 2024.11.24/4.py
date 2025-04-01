import random

def tree_generator():
    tree = []
    num_branches = random.randrange(0,4)
    branches = []
    
    for _ in range(num_branches):
        if random.choice([True, False]):
            branches.append('leaf')
        else:
            branches.append(tree_generator())
            
    return branches if branches else ['leaf']
    
#C:\Git\Sajgakova\2024.11.24>python -i 4.py
#>>> tree_generator()
#[['leaf']]
#>>> tree_generator()
#['leaf']
#>>> tree_generator()
#[['leaf'], 'leaf']
#>>> tree_generator()
#['leaf', 'leaf', ['leaf']]
#>>> tree_generator()
#[[['leaf']], ['leaf'], 'leaf']
#>>>