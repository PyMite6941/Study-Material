# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Precalculus

import math
import matplotlib.pyplot as plt
import numpy as np
import random

desire_to_solve_logs = int(input("Enter the amount of problems that you want to solve:\n> "))

# Loop for repeating problems
for i in range(desire_to_solve_logs):
    # Define variables randomly
    type_of_equation = random.choice('power_undoer','graphing_fun')

    if type_of_equation == 'power_undoer':
        # Randomly choose variables
        b = random.randint(2,16)
        y = round(random.randint(0,1001),2)
        form_choosing_number = random.randint(0, 501)
        equation_choosing_number = random.randint(0, 501)

        # Define variables to solve the equation
        type_of_equation = 'ln' if form_choosing_number%2==0 else 'log'
        base_of_equation =  b if type_of_equation == math.log else math.e
        equation = f'{type_of_equation}_{base_of_equation}({y}) = ?' if equation_choosing_number%2==0 else f'{type_of_equation}_{b}( ? ) = {y}'
        solution_of_equation = base_of_equation**y if equation_choosing_number%2==1 else math.log(y, base_of_equation)

        # Display the practice problem
        print(f"Your {type_of_equation} equation: {equation}")

        # Get user input for the equation
        x_solution_input = float(input("Enter the solution for the equation:\n> "))
        print(f"{'Correct!' if x_solution_input else None}")
        
    elif type_of_equation == 'graphing_fun':
        # Define variables randomly
        a = random.randint(0,10)
        b = round(random.uniform(0.25,6.51),2)
        h = round(random.uniform(-5,5.1),2)
        k = round(random.uniform(-5,5.1),2)

        # Ask for user input
        vertical_asymptotes = str(input("Are there any vertical asymptotes (y/n) ?")).lower().strip()
        vertical_asymptote_where = str(input("Where is the vertical asymptote (x=?) ?\n> "))
        domain_input = str(input("What is the domain of the logarithm (x=?) ?\n>")).lower().strip()

        # Check user inputs
        print(f"Correct! x={h}" if vertical_asymptotes == 'y' and vertical_asymptote_where == f'x={h}' else (f"Incorrect,... x={h}" if vertical_asymptotes =='n' or vertical_asymptote_where != h else "Incorrect... there is a vertical asymptote"))

        # Graph the equation if desired
        _continue = str(input("Continue to graph (y/n) ?\n> ")).lower().strip()
        if _continue == 'y':
            # Configuration settings
            x = np.linspace(0.1, 10, 500)
            y = np.log(x)/np.log(b)
            plt.figure(figsize=(10,6))
            plt.grid(True,alpha=0.3)
            plt.legend(fontsize=10)
            plt.ylim(k-20,k+20)
            plt.xlim(h-20,h+20)
            plt.title(f'Logarithm Graph (log_{b})',fontsize=14)

            # Create the graph
            plt.plot(x,y,'b-',linewidth=2,label=f'y = log_{b}')
            plt.plot(h,k,'go',markersize=10,label=f'Vertex: ({h:.2f}, {k:.2f})',color='blue')
            
            # Display the graph
            plt.show()