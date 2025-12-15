# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Precalculus

import math
import matplotlib.pyplot as plt
import numpy as np
import random

desire_to_solve_quadratics = int(input("How many practice questions do you want to solve?\n> "))

# Loop for repeating problems
for i in range(desire_to_solve_quadratics):
    # Define variables randomly
    a = random.randint(1,10)
    b = random.randint(0,51)
    c = random.randint(0,76)

    # Display the practice problem
    print(f"Your quadratric equation: {a}x^2+{b}x+{c}")

    # Get and store user input
    discriminant_input = float(input("Solve for the descriminant:\n> "))
    possible_to_solve_input = str(input("Is it possible to solve this problem using real numbers? (yes or no)\n> ")).lower().strip()
    if possible_to_solve_input == 'yes':
        amount_of_x_values_input = int(input("How many x values are possible?\n> "))
        x_values_input = []
        for i in range(amount_of_x_values_input):
            x_value_input = float(input(f"Enter the {i+1} x value:\n> "))
            x_values_input.append(x_value_input)
        y_int_input = int(input("Solve for the y-intercept:\n> "))
        vertex_coords_input = tuple(map(float, input("Solve for the vertex (seperate the x and y with spaces):\n> ")))
        vertex_form_raw_input = input("What is the vertex form (ax^2+bx+c) ?\n> ")
        try:
            vertex_form_input = str(vertex_form_raw_input).lower().strip()
        except ValueError as e:
            print(f"Error: {e}")
        direction_input = str(input("What direction does the parabola face (up or down) ?\n> ")).lower().strip()
    
    # Check to see if solving the equation is possible
    discriminant = float((b**2)-4*a*c)
    if discriminant >= 0:
        possible_to_solve = True
    else:
        possible_to_solve = False

    # If possible, solve the equation for the desired variables
    if possible_to_solve == True:
        amount_of_x_values = 2 if discriminant > 0 else (1 if discriminant == 0 else 0)
        x_values = []
        try:
            x_value_1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
            x_values.append(x_value_1)
            x_value1_exists = True
        except ValueError:
            x_value1_exists = False
            pass
        try:
            x_value_2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
            x_values.append(x_value_2)
            x_value2_exists = True
        except ValueError:
            x_value2_exists = False
            pass
        h = (-b/(2*a))
        k = (a*h**2) + (b*h) + c
        vertex_form = f"{a}(x {'-' if h > 0 else '+'} {h}) {'+' if k > 0 else '-'} {k}"
        vertex_coords = (h, k)
        direction = "up" if a > 0 else "down"

    # Check answers
    print("Answers:")
    print(f"Discriminate correct! {discriminant:.2f}" if abs(discriminant-discriminant_input) < 0.1 else f"Discriminate incorrect... {discriminant:.2f}")

    # Only display if possible_to_solve is True
    if possible_to_solve == True:
        print(f"{"Correct about possibility to solve!" if possible_to_solve_input == ('yes' if possible_to_solve else 'no') else f"Incorrect about possiblity to solve..."} {possible_to_solve}")
        print(f"{'X-values are correct!' if abs(x_values_input[0]-x_value_1) < 0.1 else 'X-values are incorrect,...'} x = {x_value_1 if x_value1_exists else ''}{',' if x_value1_exists and x_value2_exists else ''}{x_value_2 if x_value2_exists else ''}")
        print(f"Correct y-intercept! {c:.2f}" if c == y_int_input else f"Incorrect y-intercent... {c}")
        print(f"")
        
        # Graph the equation if desired
        _continue = str(input("Continue to graph (y/n) ?\n> ")).lower().strip()
        if _continue == 'y':
            # Configuration settings
            x = np.linspace(-10, 10, 500)
            y = a*(x**2)+b*x+c
            plt.figure(figsize=(10,6))
            plt.grid(True,alpha=0.3)
            plt.legend(fontsize=10)
            plt.ylim(k-20,k+20)
            plt.xlim(h-20,h+20)
            plt.title(f'Quadratic Graph ({a}*(x**2)+{b}*x+{c})',fontsize=14)

            # Create the graph
            plt.plot(x,y,'b-',linewidth=2,label=f'y = {a}*(x**2)+{b}*x+{c}')
            plt.plot(h,k,'go',markersize=10,label=f'Vertex: ({h:.2f}, {k:.2f})',color='blue')
            plt.plot(0,c,'mo',markersize=10,label=f'Y-Int: (0, {c:.2f})',color='g')

            # Display the graph
            plt.show()
        else:
            continue

    else:
        print(f"{"Correct about possibility to solve!" if possible_to_solve_input == ('no' if not possible_to_solve else 'yes') else f"Incorrect about possiblity to solve..."} {possible_to_solve}")