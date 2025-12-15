# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Precalculus

from math import degrees, asin, acos, atan
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
from sympy import sin, cos, tan, pi, Rational

desire_to_solve_trig_questions = int(input("How many trig questions do you want to solve?:\n> "))

# Loop for repeating problems
for i in range(desire_to_solve_trig_questions):
    chosen_problem_type = random.choice(['solve_triangle_measurements','exact_function_values','graphing_trig_functions'])

    # Solving angles and sides of triangles problems
    if chosen_problem_type == 'solve_triangle_measurements':        
        # Randomly assign variables
        num_total_given = random.randint(1,3)
        given_info = random.sample(['a','b','c','A','B'], num_total_given)

        given_sides = [sides for sides in given_info if sides in ['a','b','c']]
        given_angles = [angles for angles in given_info if angles in ['A','B']]
        solvable = (len(given_sides) >= 1) and ((len(given_sides) + len(given_angles)) >= 2)
        C = 90  # Right angle
        
        # Display the triangle
        print(f"Triangle:\n          A\n          *\n         /|\n    c   / |\n       /  | a\n      /   |\n     /    |\n    /     |\n   *──────*\n   B   b   C\n")

        solvable_input = input(f"Chosen variables:\n{given_info}\nIs this problem solvable (y/n) ?\n> ")

        # See if the problem is solvable
        if solvable:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} possible to solve")

            # If sides > 1 the solve
            if len(given_sides) == 2:
                # If 'a' and 'b' then solve
                if 'a' in given_sides and 'b' in given_sides:
                    a = random.randint(4,21)
                    b = random.randint(3,49)
                    print(f"Solve for side c with provided variables:\nSide A: {a} units\nSide B: {b} units\n")
                    c_input = float(input("Solve for side c (units):\n> "))
                    c_answer = (a**2 + b**2)**0.5
                    print(f"{'Correct!' if abs(c_input-c_answer) < 0.1 else 'Incorrect,...'} {c_answer}")
                    if not 'A' in given_info:
                        A_input = float(input("Solve for angle A (radians):\n> "))
                        A_answer = Rational(degrees(asin(a/c_answer)),180)*pi
                        print(f"{'Correct!' if abs(A_input-A_answer) < 0.1 else 'Incorrect,...'} {A_answer}")
                    if not 'B' in given_info:
                        B_input = float(input("Solve for angle B (radians):\n> "))
                        B_answer = Rational(degrees(asin(b/c)),180)*pi
                        print(f"{'Correct!' if abs(B_input-B_answer) < 0.1 else 'Incorrect,...'} {B_answer}")

                # If 'a' and 'c' then solve
                elif 'a' in given_sides and 'c' in given_sides:
                    a = random.randint(4,21)
                    c = random.randint(13, 57) if a < 13 else random.randint(a+1, 57)
                    print(f"Solve for side b with provided variables:\nSide A: {a} units\nSide C: {c} units\n")
                    b_input = float(input("Solve for side b (units):\n> "))
                    b_answer = (c**2 - a**2)**0.5
                    print(f"{'Correct!' if abs(b_input-b_answer) < 0.1 else 'Incorrect,...'} {b_answer}")
                    if not 'A' in given_info:
                        A_input = float(input("Solve for angle A (radians):\n> "))
                        A_answer = Rational(degrees(asin(a/c)),180)*pi
                        print(f"{'Correct!' if abs(A_input-A_answer) < 0.1 else 'Incorrect,...'} {A_answer}")
                    if not 'B' in given_info:
                        B_input = float(input("Solve for angle B (radians):\n> "))
                        B_answer = Rational(degrees(asin(b_answer/c)),180)*pi
                        print(f"{'Correct!' if abs(B_input-B_answer) < 0.1 else 'Incorrect,...'} {B_answer}")

                # If 'b' and 'c' then solve
                elif 'b' in given_sides and 'c' in given_sides:
                    b = random.randint(3,19)
                    c = random.randint(13,57) if b < 13 else random.randint(b+1,57)
                    print(f"Solve for side a with provided variables:\nSide B: {b} units\nSide C: {c} units\n")
                    a_input = float(input("Solve for side a (units):\n> "))
                    a_answer = (c**2 - b**2)**0.5
                    print(f"{'Correct!' if abs(a_input-a_answer) < 0.1 else 'Incorrect,...'} {a_answer}")
                    if not 'A' in given_info:
                        A_input = float(input("Solve for angle A (radians):\n> "))
                        A_answer = Rational(degrees(asin(a_answer/c)),180)*pi
                        print(f"{'Correct!' if abs(A_input-A_answer) < 0.1 else 'Incorrect,...'} {A_answer}")
                    if not 'B' in given_info:
                        B_input = float(input("Solve for angle B (radians):\n> "))
                        B_answer = Rational(degrees(asin(b/c)),180)*pi
                        print(f"{'Correct!' if abs(B_input-B_answer) < 0.1 else 'Incorrect,...'} {B_answer}")

            # If sides == 1 and angles == 1 then solve
            elif (len(given_sides) == 1 and len(given_angles) == 1):
                # If side 'a' and angle 'A' then solve
                if 'a' in given_sides and 'A' in given_angles:
                    a = random.randint(4,21)
                    A = Rational(random.randint(15,75),180)*pi
                    print(f"Solve for side b and c with provided variables:\nSide A: {a} units\nAngle A: {A} radians\n")
                    b_input = float(input("Solve for side b (units):\n> "))
                    c_input = float(input("Solve for side c (units):\n> "))
                    b_answer = a * tan(A)
                    c_answer = a / cos(A)
                    print(f"{'Correct!' if abs(b_input-b_answer) < 0.1 else 'Incorrect,...'} {b_answer}")
                    print(f"{'Correct!' if abs(c_input-c_answer) < 0.1 else 'Incorrect,...'} {c_answer}")

                # If side 'a' and angle 'B' then solve
                elif 'a' in given_sides and 'B' in given_angles:
                    a = random.randint(4,21)
                    B = Rational(random.randint(15,75),180)*pi
                    print(f"Solve for side b and c with provided variables:\nSide A: {a} units\nAngle B: {B} radians\n")
                    b_input = float(input("Solve for side b (units):\n> "))
                    b_answer = a / tan(B)
                    print(f"{'Correct!' if abs(b_input-b_answer) < 0.1 else 'Incorrect,...'} {b_answer}")
                    c_input = float(input("Solve for side c (units):\n> "))
                    c_answer = a / sin(B)
                    print(f"{'Correct!' if abs(c_input-c_answer) < 0.1 else 'Incorrect,...'} {c_answer}")

                # If side 'b' and angle 'A' then solve
                elif 'b' in given_sides and 'A' in given_angles:
                    b = random.randint(3,19)
                    A = Rational(random.randint(15,75),180)*pi
                    print(f"Solve for side a and c with provided variables:\nSide B: {b} units\nAngle A: {A} radians\n")
                    a_input = float(input("Solve for side a (units):\n> "))
                    a_answer = b / tan(A)
                    print(f"{'Correct!' if abs(a_input-a_answer) < 0.1 else 'Incorrect,...'} {a_answer}")
                    c_input = float(input("Solve for side c (units):\n> "))
                    c_answer = b / sin(A)
                    print(f"{'Correct!' if abs(c_input-c_answer) < 0.1 else 'Incorrect,...'} {c_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")

    # Solving exact trig values on the unit circle
    elif chosen_problem_type == 'exact_function_values':
        # Randomly assign variables
        trig_values = random.choice(['sin','cos','tan','csc','sec','cot'])
        angle = Rational(random.choice([30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360]),180)*pi

        # Get user input and solve
        trig_input = input(f"What is the exact value of {trig_values} at {angle} (undefined if not possible) ?\n> ")
        try:
            trig_answer = sin(angle) if trig_values == 'sin' else (cos(angle) if trig_values == 'cos' else (tan(angle) if trig_values == 'tan' else (1/sin(angle) if trig_values == 'csc' else (1/cos(angle) if trig_values == 'sec' else 1/tan(angle)))))
        except ZeroDivisionError:
            trig_answer = 'undefined'
        print(f"{'Correct!' if trig_input == trig_answer else f'Incorrect,...'} {trig_answer}")

    elif chosen_problem_type == 'graphing_trig_functions':
        # Randomly assign variables
        trig_values = random.choice(['sin','cos','tan','csc','sec','cot'])