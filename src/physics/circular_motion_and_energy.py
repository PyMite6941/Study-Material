# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms

import math
import random

desire_to_do_circular_motion_and_energy = int(input("Enter how many problems to solve about circular motion and energy:\n> "))

# Loop for repeating problems
for i in range(desire_to_do_circular_motion_and_energy):
    # Choose a random problem type to solve for
    chosen_problem_type = random.choice(['tangential_velocity','centripetal_acceleration','centripetal_force'])
    
    # If tangential velocity then solve
    if chosen_problem_type == 'tangential_velocity':
        # Randomly choose variables to use
        num_variables = random.randint(1,3)
        chosen_variables = random.sample(['r','t','v_t',],num_variables)

        solvable_input = input(f"Solve with these variables: {chosen_variables}\nIs it possible to solve this problem (y/n) ?\n> ").lower().strip()

        # See if the problem is solvable
        if num_variables > 1:
            print("Correct, possible to solve!" if solvable_input == 'y' else "Incorrect, possible to solve...")
            
            # If radius and time then solve for velocity
            if 'r' in chosen_variables and 't' in chosen_variables:
                r = random.randint(1, 46)
                t = round(random.uniform(1, 5.1),2)
                print(f"Solve for velocity with provided variables:\nRadius: {r}\nTime: {t}\n")
                velocity_input = float(input("Solve for the tangential velocity (m/s):\n> "))
                velocity_answer = (2*math.pi*r)/t
                print(f"Correct! {velocity_answer}" if abs(velocity_answer-velocity_input) < 0.1 else f"Incorrect,..., {velocity_answer}")

            # If radius and velocity then solve for time
            elif 'r' in chosen_variables and 'v_t' in chosen_variables:
                r = random.randint(1, 46)
                v_t = round(random.uniform(5,60.1),2)
                print(f"Solve for time with provided variables:\nRadius: {r}\nVelocity: {v_t}\n")
                time_input = float(input("Solve for time (sec):\n> "))
                time_answer = (2*math.pi*r)/t
                print(f"Correct! {time_answer}" if abs(time_answer-time_input) < 0.1 else f"Incorrect,... {time_answer}")

            # If time and velocity then solve for radius
            elif 't' in chosen_variables and 'v_t' in chosen_variables:
                t = round(random.uniform(1, 5.1),2)
                v_t = round(random.uniform(5,60.1),2)
                print(f"Solve for radius with provided variables:\nTime: {t}\nVelocity: {v_t}\n")
                radius_input = float(input("Solve for radius (m):\n> "))
                radius_answer = (v_t*t)/(2*math.pi)
                print(f"Correct! {radius_answer}" if abs(radius_answer-radius_input) < 0.1 else f"Incorrect,... {radius_answer}")

        else:
            print("Correct, not possible to solve!" if solvable_input == 'n' else "Incorrect, possible to solve...")

    # If centripetal acceleartion then solve
    elif chosen_problem_type == 'centripetal_acceleration':
        # Randomly choose variables to use
        num_variables = random.randint(1,3)
        chosen_variables = random.sample(['a','r','v_t'],num_variables)

        solvable_input = input(f"Solve with these variables: {chosen_variables}\nIs it possible to solve this problem (y/n) ?\n> ").lower().strip()

        # See if the problem is solvable
        if num_variables > 1:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} the problem is solvable")

            # If 'a' and 'r' then solve
            if 'a' in chosen_variables and 'r' in chosen_variables:
                a = round(random.uniform(1,66),2)
                r = random.randint(1, 46)
                print(f"Solve for velocity with the provided variables:\nAcceleration: {a} m/s^2\nRadius: {r} m\n")
                v_t_input = float(input("Solve for velocity (m/s):\n> "))
                v_t_answer = math.sqrt(a*r)
                print(f"{'Correct!' if abs(v_t_answer-v_t_input) < 0.1 else 'Incorrect,...'} {v_t_answer}")

            # If 'a' and 'v_t' then solve
            elif 'a' in chosen_variables and 'v_t' in chosen_variables:
                a = round(random.uniform(1,66),2)
                v_t = round(random.uniform(0,100.1),2)
                print(f"Solve for radius with provided variables:\nAcceleration: {a} m/s^2\nVelocity: {v_t} m/s\n")
                r_input = float(input("Solve for radius (m):\n> "))
                r_answer = (v_t**2)/a
                print(f"{'Correct!' if abs(r_answer-r_input) < 0.1 else 'Incorrect,...'} {r_answer}")

            # If 'r' and 'v_t' then solve
            elif 'r' in chosen_variables and 'v_t' in chosen_variables:
                r = random.randint(1, 46)
                v_t = round(random.uniform(0,100.1),2)
                print(f"Solve for acceleration with provided variables:\nRadius: {r} m\nVelocity: {v_t} m/s")
                a_input = float(input("Solve for acceleration (m/s^2):\n> "))
                a_answer = (v_t**2)/r
                print(f"{'Correct!' if abs(a_answer-a_input) < 0.1 else 'Incorrect,...'} {a_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} the problem is not solvable")

    # If none of the above
    else:
        # Randomly choose variables to use
        num_variables = random.randint(1, 3)
        chosen_variables = random.sample(['a','F','m'],num_variables)

        solvable_input = input(f"Solve with these variables: {chosen_variables}\nIs it possible to solve this problem (y/n) ?\n> ").lower().strip()

        # See if the problem is solvable
        if num_variables > 1:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} possible to solve")

            # If 'a' and 'F' then solve
            if 'a' in chosen_variables and 'F' in chosen_variables:
                a = round(random.uniform(1,66),2)
                F = round(random.uniform(10,10000),2)
                print(f"Solve for mass with provided variables:\nAcceleration: {a} m/s^2\nNet Force: {F} N\n")
                m_input = float(input("Solve for mass (kg):\n> "))
                m_answer = F/a
                print(f"{'Correct!' if abs(m_answer-m_input) < 0.1 else 'Incorrect,...'} {m_answer}")

            # If 'a' and 'm' then solve
            elif 'a' in chosen_variables and 'm' in chosen_variables:
                a = round(random.uniform(1,66),2)
                m = round(random.uniform(0.5,1000.1),2)
                print(f"Solve for net force with provided variables:\nAcceletation: {a} m/s^2\nMass: {m} kg\n")
                F_input = float(input("Solve for net force (N):\n> "))
                F_answer = m*a
                print(f"{'Correct!' if abs(F_answer-F_input) < 0.1 else 'Incorrect,...'} {F_answer}")

            # If 'F' and 'm' then solve
            elif 'F' in chosen_variables and 'm' in chosen_variables:
                F = round(random.uniform(10,10000),2)
                m = round(random.uniform(0.5,1000.1),2)
                print(f"Solve for acceleration with provided variables:\nNet Force: {F} N\nMass: {m} kg\n")
                a_input = float(input("Solve for acceleration (m/s^2):\n> "))
                a_answer = F/m
                print(f"{'Correct!' if abs(a_answer-a_input) < 0.1 else 'Incorrect,...'} {a_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")