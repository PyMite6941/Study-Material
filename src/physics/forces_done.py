# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Conceptual Physics

import random

desire_to_solve_forces_done = int(input("How many problems do you want to solve?:\n> "))

# Loop for repeating problems
for i in range(desire_to_solve_forces_done):
    chosen_problem_type = random.choice(['gravitational_force','normal_force','spring_force','tension_force'])

    # Gravitational Force problems
    if chosen_problem_type == 'gravitational_force':
        # Randomly assign variables
        num_variables = random.randint(1,3)
        chosen_variables = random.sample(['Fg','g','m'])

        solvable_input = input(f"Chosen variables:\n{chosen_variables}\nIs this problem solvable (y/n) ?\n> ")

        # See if the problem is solvable
        if num_variables > 1:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrrect,...'} possible to solve")

            # If 'Fg' and 'g' then solve
            if 'Fg' in chosen_variables and 'g' in chosen_variables:
                Fg = round(random.uniform(0.2,1000.1),2)
                g = 10
                print(f"Solve for mass with provided variables:\nForce of Gravity: {Fg} N\nAcceleration of Gravity: {g} m/s^2")
                m_input = float(input("Solve for mass (kg):\n> "))
                m_answer = Fg/g
                print(f"{'Correct!' if abs(m_answer-m_input) < 0.1 else 'Incorrect,...'} {m_answer}")

            # If 'Fg' and 'm' then solve
            elif 'Fg' in chosen_variables and 'm' in chosen_variables:
                Fg = round(random.uniform(0.2,1000.1),2)
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for acceleration of gravitatity with provided variables:\nForce of Gravity: {Fg} N\nMass: {m} kg\n")
                g_input = float(input("Solve for acceleration of gravity (m/s^2):\n> "))
                g_answer = Fg/m
                print(f"{'Correct!' if abs(g_answer-g_input) < 0.1 else 'Incorrect,...'} {g_answer}")

            # If 'g' and 'm' then sovle
            elif 'g' in chosen_variables and 'm' in chosen_variables:
                g = 10
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for force of gravity with provided variables:\nAcceleration of Gravity: {g} m/s^2\nMass: {m} kg\n")
                Fg_input = float(input("Solve for force of gravity (N):\n> "))
                Fg_answer = m*g
                print(f"{'Correct!' if abs(Fg_answer-Fg_input) < 0.1 else 'Incorrect,...'} {Fg_answer}")


        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")

    # Normal Force problems
    if chosen_problem_type == 'normal_force':
        # Randomly assign variables
        num_variables = random.randint(1,3)
        chosen_variables = random.sample(['Fn','g','m'])

        solvable_input = input(f"Chosen variables:\n{chosen_variables}\nIs this problem solvable (y/n) ?\n> ")

        # See if the problem is solvable
        if num_variables > 1:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrrect,...'} possible to solve")

            # If 'Fn' and 'g' then solve
            if 'Fn' in chosen_variables and 'g' in chosen_variables:
                Fn = round(random.uniform(0.2,1000.1),2)
                g = 10
                print(f"Solve for mass with provided variables:\nNormal Force: {Fn} N\nAcceleration of Gravity: {g} m/s^2")
                m_input = float(input("Solve for mass (kg):\n> "))
                m_answer = Fn/g
                print(f"{'Correct!' if abs(m_answer-m_input) < 0.1 else 'Incorrect,...'} {m_answer}")

            # If 'Fn' and 'm' then solve
            elif 'Fn' in chosen_variables and 'm' in chosen_variables:
                Fn = round(random.uniform(0.2,1000.1),2)
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for acceleration of gravitatity with provided variables:\nNormal Force: {Fn} N\nMass: {m} kg\n")
                g_input = float(input("Solve for acceleration of gravity (m/s^2):\n> "))
                g_answer = Fn/m
                print(f"{'Correct!' if abs(g_answer-g_input) < 0.1 else 'Incorrect,...'} {g_answer}")

            # If 'g' and 'm' then sovle
            elif 'g' in chosen_variables and 'm' in chosen_variables:
                g = 10
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for normal force with provided variables:\nAcceleration of Gravity: {g} m/s^2\nMass: {m} kg\n")
                Fn_input = float(input("Solve for normal force (N):\n> "))
                Fn_answer = m*g
                print(f"{'Correct!' if abs(Fn_answer-Fn_input) < 0.1 else 'Incorrect,...'} {Fg_answer}")


        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")

    # Spring Force problems
    elif chosen_problem_type == 'spring_force':
        # Randomly assign variables
        num_variables = random.randint(1,3)
        chosen_variables = random.sample(['Fs','k','x'],num_variables)

        solvable_input = input(f"Chosen variables:\n{chosen_variables}\nIs this problem solvable (y/n) ?\n> ")

        # See if the problem is solvable
        if num_variables > 1:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} possible to solve")

            # If 'Fs' and 'k' then solve
            if 'Fs' in chosen_variables and 'k' in chosen_variables:
                Fs = round(random.uniform(0.2,1000.1),2)
                k = round(random.uniform(50,500),2)
                print(f"Solve for compression distance with provided variables:\nSpring Force: {Fs} N\nSpring Constant: {k} N/m\n")
                x_input = float(input("Solve for compression distance (m):\n> "))
                x_answer = Fs/k
                print(f"{'Correct!' if abs(x_answer-x_input) < 0.1 else 'Incorrect,...'} {x_answer}")

            # If 'Fs' and 'x' then solve
            if 'Fs' in chosen_variables and 'x' in chosen_variables:
                Fs = round(random.uniform(0.2,1000.1),2)
                x = round(random.uniform(0.1, 2.1),2)
                print(f"Solve for spring constant with provided variables:\nSpring Force: {Fs} N\nCompression Distance: {x} m\n")
                k_input = float(input("Solve for spring constant (N/m):\n> "))
                k_answer = Fs/x
                print(f"{'Correct!' if abs(k_answer-k_input) < 0.1 else 'Incorrect,...'} {k_answer}")

            # If 'k' and 'x' then solve
            if 'k' in chosen_variables and 'x' in chosen_variables:
                k = round(random.uniform(50,500),2)
                x = round(random.uniform(0.1, 2.1),2)
                print(f"Solve for spring force with provided variables:\nSpring Constant: {k} N/m\nCompression Distance: {x} m\n")
                Fs_input = float(input("Solve for spring force (N):\n> "))
                Fs_answer = k*x
                print(f"{'Correct!' if abs(Fs_answer-Fs_input) < 0.1 else 'Incorrect,...'} {Fs_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")

    # Tension Force problems
    else:
        # Randomly assign variables
        num_variables = random.randint(2, 4)
        chosen_variables = random.sample(['a','Fg','Ft','m'],num_variables)

        solvable_input = input(f"Chosen variables:\n{chosen_variables}\nIs this problem solvable (y/n) ?\n> ")

        if num_variables > 2:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} possible to solve")

            # If 'a' and 'Fg' and 'Ft' then solve
            if 'a' in chosen_variables and 'Fg' in chosen_variables and 'Ft' in chosen_variables:
                a = round(random.uniform(1,66),2)
                Fg = round(random.uniform(0.2,1000.1),2)
                Ft = round(random.uniform(0.2,1000.1),2)
                print(f"Solve for mass with provided variables:\nAcceleration: {a} m/s^2\nForce of Gravity: {Fg} N\nTension Force: {Ft} N\n")
                m_input = float(input("Solve for mass (kg):\n> "))
                m_answer = (Ft-Fg)/a
                print(f"{'Correct!' if abs(m_answer-m_input) < 0.1 else 'Incorrect,...'} {m_answer}")

            # If 'a' and 'Fg' and 'm' then solve
            elif 'a' in chosen_variables and 'Fg' in chosen_variables and 'm' in chosen_variables:
                a = round(random.uniform(1,66),2)
                Fg = round(random.uniform(0.2,1000.1),2)
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for force of tension with provided variables:\nAcceleration: {a} m/s^2\nForce of Gravity: {Fg} N\nMass: {m} kg\n")
                Ft_input = float(input("Solve for force of tension (N):\n> "))
                Ft_answer = Fg+m*a
                print(f"{'Correct!' if abs(Ft_answer-Ft_input) < 0.1 else 'Incorrect,...'} {Ft_answer}")

            # If 'a' and 'Ft' and 'm' then solve
            elif 'a' in chosen_variables and 'Ft' in chosen_variables and 'm' in chosen_variables:
                a = round(random.uniform(1,66),2)
                Ft = round(random.uniform(0.2,1000.1),2)
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for force of gravity with provided variables:\nAcceleration: {a}\nForce of Tension: {Ft}\nMass: {m} kg\n")
                Fg_input = float(input("Solve for force of gravity (N):\n> "))
                Fg_answer = Ft-m*a
                print(f"{'Correect!' if abs(Fg_answer-Fg_input) < 0.1 else 'Incorrect,...'} {Fg_answer}")

            # If 'Fg' and 'Ft' and 'm' then solve
            elif 'Fg' in chosen_variables and 'Ft' in chosen_variables and 'm' in chosen_variables:
                Fg = round(random.uniform(0.2,1000.1),2)
                Ft = round(random.uniform(0.2,1000.1),2)
                m = round(random.uniform(0.5,100.1),2)
                print(f"Solve for acceleration with provided variables:\nForce of Gravity: {Fg} N\nTension Force: {Ft} N\nMass: {m} kg\n")
                a_input = float(input("Solve for acceleration (m/s^2):\n> "))
                a_answer = (Ft-Fg)/m
                print(f"{'Correct!' if abs(a_answer-a_input) < 0.1 else 'Incorrect,...'} {a_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")