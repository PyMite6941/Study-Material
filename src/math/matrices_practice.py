# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before the final exam
#
# Subject: Conceptual Physics

import numpy as np
import random

desire_to_solve_matrices = int(input("How many matrices practice problems do you want to complete?\n> "))
for _ in range(desire_to_solve_matrices):
    perfect_matrices = random.choice(True,False)
    if perfect_matrices:
        problem_choice = random.sample(['addition','subtraction','multiplication','row_operations','rref'])

        if problem_choice == 'addition' or problem_choice == 'subtraction' or problem_choice == 'multiplication' or problem_choice == 'matrices_division':
            size = random.choice(2,3)
            A = np.random.randint(-5,6,(size,size))
            B = np.random.randint(-5,6,(size,size))
            print(f"Matrix A:\n{A}\n\nMatrix B:\n{B}\n")
            operations_text = {
                'addition': 'Add these matrices',
                'subtraction': 'Subtract these matrices',
                'multiplication': 'Multiply these matrices',
            }
            print(operations_text[problem_choice])

            answer = A+B if problem_choice == 'addition' else (A-B if problem_choice == 'subtraction' else (A@B if problem_choice == 'multiplication' else A/B))
