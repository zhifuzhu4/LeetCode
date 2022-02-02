"""
Randomly select problems for practice
"""

import os
import random

# get list of problems
problems = [x.split('.')[0].replace('_', ' ') for x in os.listdir() if x.endswith('.py')]
print(f'Total problems: {len(problems)}')

# randomly select one problem
to_solve = random.choice(problems)
print(f'Please solve problem: {to_solve}')

f = open(to_solve.replace(' ', '_') + ".py", "r")
print(f.readlines(4))

