# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Conceptual Physics

import math
import random

desire_to_do_physics = int(input("How many practice problems do you want to solve?\n> "))

# Loop for repeating problems
for i in range(desire_to_do_physics):
    # Choose challenge type
    chosen_problem_type = random.choice(['single_energy','energy_conservation','momentum','calculating_total_work','total_mechanical_energy'])

    # Problems involving one energy type
    if chosen_problem_type == 'single_energy':
        energy_type = random.choice(['epe','gpe','ke'])

        # Define universal variables
        m = round(random.uniform(1,1000.1),2)
        g = 10

        if 'gpe' in energy_type:
            h = random.randint(0,30)
            print(f"Solve for GPE with provided variables:\nMass: {m} kg\nHeight: {h} m\nGravitational Acceleation: {g} m/s^2\n")
            gpe_input = float(input("Solve for GPE (J):\n> "))
            gpe_answer = m*g*h
            print(f"{"Correct!" if abs(gpe_answer-gpe_input) < 0.1 else "Incorrect,..."} {gpe_answer:.2f}\n")

        elif 'ke' in energy_type:
            v = round(random.uniform(0,100),2)
            print(f"Solve for KE with provided variables:\nMass: {m} kg\nVelocity: {v} m/s\n")
            ke_input = float(input("Solve for KE (J):\n> "))
            ke_answer = (1/2)*m*v**2
            print(f"{"Correct!" if abs(ke_answer-ke_input) < 0.1 else "Incorrect,..."} {ke_answer:.2f}\n")

        elif 'epe' in energy_type:
            k = round(random.uniform(50,500),2)
            x = round(random.uniform(0.1, 2.1),2)
            print(f"Solve for EPE with provided variables:\nSpring Constant: {k} N*m\nCompression Distance: {x} m\n")
            epe_input = float(input("Solve for EPE (J):\n> "))
            epe_answer = (1/2)*k*x**2
            print(f"{"Correct!" if abs(epe_answer-epe_input) < 0.1 else "Incorrect,..."} {epe_answer:.2f}\n")

    # Problems converting from one energy type to another (no loss)
    elif chosen_problem_type == 'energy_conservation':
        # Randomly choose variables to use
        num_initial_variables = random.randint(1,3)
        num_final_variables = random.randint(1,3)
        inital_variables = random.sample(['epe','gpe','ke'],num_initial_variables)
        final_variables = random.sample(['epe','gpe','ke'],num_final_variables)

        print(f"Convert {inital_variables} to {final_variables}")
        
        # Define universal variables
        m = round(random.uniform(0,100.1),2)
        g = 10
        
        # Generate variables
        if 'gpe' in inital_variables:
            h_i = random.randint(0,30)
            print(f"Solve for GPE_i with provided variables:\nMass: {m} m\nInitial Height: {h_i} m\nGravitational Acceleration: {g} m/s^2\n")
            gpe_i_input = float(input("Solve for GPE_i (J):\n> "))
            gpe_i_answer = m*g*h_i
            print(f"{"Correct!" if abs(gpe_i_answer-gpe_i_input) < 0.1 else "Incorrect,..."} {gpe_i_answer:.2f}\n")

        if 'ke' in inital_variables:
            v_i = round(random.uniform(0,50),2)
            print(f"Solve for KE_i with provided variables:\nMass: {m} kg\nInitial Velocity: {v_i} m/s\n")
            ke_i_input = float(input("Solve for KE_i (J):\n> "))
            ke_i_answer = (1/2)*m*v_i**2
            print(f"{"Correct!" if abs(ke_i_answer-ke_i_input) < 0.1 else "Incorrect,..."} {ke_i_answer:.2f}\n")

        if 'epe' in inital_variables:
            k_i = round(random.uniform(50,500),2)
            x_i = round(random.uniform(0.1, 2.1),2)
            print(f"Spring Constant: {k_i} N/m\nDisplacement: {x_i} m\n")
            epe_i_input = float(input("Solve for EPE (J):\n> "))
            epe_i_answer = (1/2)*k_i*x_i**2
            print(f"{"Correct!" if abs(epe_i_answer-epe_i_input) < 0.1 else f"EPE is incorrect..."} {epe_i_answer:.2f}\n")

        if 'gpe' in final_variables:
            h_f = random.randint(0,30)
            print(f"Solve for GPE_f with provided variables:\nMass: {m} kg\nFinal Height: {h_f} m\nGravitational Acceleration: {g} m/s^2\n")
            gpe_f_input = float(input("Solve for GPE_f (J):\n> "))
            gpe_f_answer = m*g*h_f
            print(f"{"Correct!" if abs(gpe_f_answer-gpe_f_input) < 0.1 else "Incorrect,..."} {gpe_f_answer:.2f}\n")

        if 'ke' in final_variables:
            v_f = round(random.uniform(0,50),2)
            print(f"Solve for KE_f with provided variables:\nMass: {m} kg\nFinal Velocity: {v_f} m/s\n")
            ke_f_input = float(input("Solve for KE_f (J):\n> "))
            ke_f_answer = (1/2)*m*v_f**2
            print(f"{"Correct!" if abs(ke_f_answer-ke_f_input) < 0.01 else "Incorrect,..."} {ke_f_answer:.2f}\n")
            
        if 'epe' in final_variables:
            k_f = round(random.uniform(50,500),2)
            x_f = round(random.uniform(0.1, 2.1),2)
            print(f"Solve for EPE_f with provided variables:\nSpring Constant: {k_f} N/m\nDisplacement: {x_f} m\n")
            epe_f_input = input("Solve for EPE (J):\n> ")
            epe_f_answer = (1/2)*k_f*x_f**2
            print(f"{"EPE is correct!" if abs(epe_f_answer-epe_f_input) < 0.1 else f"EPE is incorrect..."} {epe_f_answer:.2f}\n")

    # Problems about momentum
    elif chosen_problem_type == 'momentum':
        # Randomly choose variables to use
        num_variables = random.randint(1,3)
        selected_variables = random.sample(['m','p','v'],num_variables)
        
        print(f"Solve with provided variable(s):\n{selected_variables}")
        solvable_input = input("Is it possible to solve this problem (y/n) ?\n> ").lower().strip()
        
        # See if the problem is solvable
        if num_variables > 1:
            print("Correct! possible to solve" if solvable_input == 'y' else "Incorrect,... possible to solve")

            # If mass and momentum then solve for speed
            if 'm' in selected_variables and 'p' in selected_variables:
                m = round(random.uniform(1,100.1),2)
                p = round(random.uniform(100,1000),2)
                print(f"Solve for speed with provided variables:\nMass: {m} kg\nMomentum: {p} kg*m/s\n")
                speed_input = float(input("Solve for speed (m/s):\n> "))
                speed_answer = p/m
                print(f"{"Correct!" if abs(speed_answer-speed_input) < 0.1 else "Incorrect,..."} {speed_answer:.2f}\n")
            
            # If mass and speed then solve for momentum
            elif 'm' in selected_variables and 'v' in selected_variables:
                m = round(random.uniform(0.5,100.1),2)
                v = round(random.uniform(0,50),2)
                print(f"Solve for momentum with provided variables:\nMass: {m} kg\nSpeed: {v} m/s\n")
                momentum_input = float(input("Solve for momentum (kg*m/s):\n> "))
                momentum_answer = m*v
                print(f"{"Correct!" if abs(momentum_answer-momentum_input) < 0.1 else f"Incorrect..."} {momentum_answer:.2f}\n")
            
            # If speed and momentum then solve for mass
            elif 'v' in selected_variables and 'p' in selected_variables:
                p = round(random.uniform(100,1000),2)
                v = round(random.uniform(0.5,50.1),2)
                print(f"Solve for mass with provided variables:\nMomentum: {p} kg*m/s\nSpeed: {v} m/s\n")
                mass_input = float(input("Solve for mass (kg):\n> "))
                mass_answer = p/v
                print(f"{"Correct!" if abs(mass_answer-mass_input) < 0.1 else f"Incorrect..."} {mass_answer:.2f}\n")
        
        else:
            print("Correct! not possible to solve" if solvable_input == 'n' else "Incorrect,... not possible to solve")

    # Problems about Calculating Work
    elif chosen_problem_type == 'calculating_total_work':
        # Randomly choose variables to use
        num_variables = random.randint(2,4)
        selected_variables = random.sample(['angle','d','F','W'],num_variables)

        solvable_input = input(f"Provided variables:\n{selected_variables}\nIs this problem solvable (y/n) ?\n> ")

        # See if the problem is solvable
        if num_variables > 3:
            print(f"{'Correct!' if solvable_input == 'y' else 'Incorrect,...'} possible to solve")

            if 'angle' in selected_variables and 'd' in selected_variables and 'F' in selected_variables:
                angle = random.choice([90,0,-90])
                d = round(random.uniform(3,25.1),2)
                F = round(random.uniform(50,5000.1),2)
                print(f"Solve for work with provided variables:\nAngle: {angle} degrees\nDisplacement: {d} m\nForce: {F} N\n")
                work_input = float(input("Solve for work (J):\n> "))
                work_answer = F*d*math.cos(angle)
                print(f"{'Correct!' if abs(work_answer-work_input) < 0.1 else 'Incorrect,...'} {work_answer}")

            elif 'angle' in selected_variables and 'd' in selected_variables and 'W' in selected_variables:
                angle = random.choice([90,0,-90])
                d = round(random.uniform(3,25.1),2)
                W = round(random.uniform(100,1000.1),2)
                print(f"Solve for force with provided variables:\nAngle: {angle} degrees\nDisplacement: {d} m\nWork: {W} J\n")
                force_input = float(input("Solve for force (N):\n> "))
                force_answer = W/(d*math.cos(angle))
                print(f"{'Correct!' if abs(force_answer-force_input) < 0.1 else 'Incorrect,...'} {force_answer}")

            elif 'angle' in selected_variables and 'F' in selected_variables and 'W' in selected_variables:
                angle = random.choice([90,0,-90])
                F = round(random.uniform(50,5000.1),2)
                W = round(random.uniform(100,1000.1),2)
                print(f"Solve for displacement with provided variables:\nAngle: {angle} degrees\nForce: {F} N\nWork: {W} J\n")
                d_input = float(input("Solve for displacement (m):\n> "))
                d_answer = W/(F*math.cos(angle))
                print(f"{'Correct!' if abs(d_answer-d_input) < 0.1 else 'Incorrect'} {d_answer}")

            elif 'd' in selected_variables and 'F' in selected_variables and 'W' in selected_variables:
                d = round(random.uniform(3,25.1),2)
                F = round(random.uniform(50,5000.1),2)
                W = round(random.uniform(100,1000.1),2)
                print(f"Solve for angle with provided variables:\nDisplacement: {d}\nForce: {F} N\nWork: {W} J\n")
                angle_input = float(input("Solve for angle (in degrees):\n> "))
                angle_answer = math.acos(W/(F*d))
                print(f"{'Correct!' if abs(angle_answer-angle_input) < 0.1 else 'Incorrect,...'} {angle_answer}")

        else:
            print(f"{'Correct!' if solvable_input == 'n' else 'Incorrect,...'} not possible to solve")

    # Porblems about total Mechanical energy
    else:
        # Create variables to use
        m = round(random.uniform(0,100.1),2)
        g = 10

        # Randomly choose variables to solve for
        num_energies = random.randint(1, 3)
        selected_energies = random.sample(['epe','gpe','ke'], num_energies)

        # If GPE then solve
        if 'gpe' in selected_energies:
            h = random.randint(0,30)
            print(f"Solve for GPE with provided variables:\nMass: {m} kg\nHeight: {h} m\n")
            gpe_input = float(input("Solve for GPE (J):\n> "))
            gpe_answer = m*g*h
            print(f"{"GPE is correct!" if abs(gpe_answer-gpe_input) < 0.1 else f"GPE is incorrect..."} {gpe_answer:.2f}\n")

        # If KE then solve
        if 'ke' in selected_energies:
            v = round(random.uniform(0,30),2)
            print(f"Solve for KE with provided variables:\nMass: {m} kg\nVelocity: {v} m/s\n")
            ke_input = float(input("Solve for KE (J):\n> "))
            ke_answer = (1/2)*m*v**2
            print(f"{"KE is correct!" if abs(ke_answer-ke_input) < 0.1 else f"KE is incorrect..."} {ke_answer:.2f}\n")

        # If EPE then solve
        if 'epe' in selected_energies:
            k = round(random.uniform(50,500),2)
            x = round(random.uniform(0.1, 2.1),2)
            print(f"Solve for EPE with provided variables:\nSpring Constant: {k} N/m\nDisplacement: {x} m\n")
            epe_input = float(input("Solve for EPE (J):\n> "))
            epe_answer = (1/2)*k*x**2
            print(f"{"EPE is correct!" if abs(epe_answer-epe_input) < 0.1 else f"EPE is incorrect..."} {epe_answer:.2f}\n")