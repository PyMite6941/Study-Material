# Creator: Matt Gresham (aka PyMite6941)
#
# Purpose: To disguise programming as studying for precalculus so I can enjoy my time before midterms
#
# Subject: Conceptual Physics

import random

conversions = {
    # Force
    'N_to_kg*m/s^2': { 'from': 'N', 'to': 'kg*m/s^2', 'factor': 1 },
    'kg*m/s^2_to_N': { 'from': 'kg*m/s^2', 'to': 'N', 'factor': 1 },

    # Energy
    'J_to_N*m': { 'from': 'J', 'to': 'N*m', 'factor': 1 },
    'N*m_to_J': { 'from': 'N*m', 'to': 'J', 'factor': 1 },
    'J_to_kg*m^2/s^2': { 'from': 'J', 'to': 'kg*m^2/s^2', 'factor': 1 },
    'kg*m^2/s^2_to_J': { 'from': 'kg*m^2/s^2', 'to': 'J', 'factor': 1 },

    # Length
    'm_to_mm': { 'from': 'm', 'to': 'mm', 'factor': 1000 },
    'mm_to_m': { 'from': 'mm', 'to': 'm', 'factor': 0.001 },
    'm_to_cm': { 'from': 'm', 'to': 'cm', 'factor': 100 },
    'cm_to_m': { 'from': 'cm', 'to': 'm', 'factor': 0.01 },
    'm_to_km': { 'from': 'm', 'to': 'km', 'factor': 0.001 },
    'km_to_m': { 'from': 'km', 'to': 'm', 'factor': 1000 },

    # Power
    'W_to_J/s': { 'from': 'W', 'to': 'J/s', 'factor': 1 },
    'J/s_to_W': { 'from': 'J/s', 'to': 'W', 'factor': 1 },

    # Speed
    'km/hr_to_m/s': { 'from': 'km/hr', 'to': 'm/s', 'factor': 1/3.6 },
    'm/s_to_km/h': { 'from': 'm/s', 'to': 'km/h', 'factor': 3.6 },

    # Time
    'min_to_sec': { 'from': 'min', 'to': 'sec', 'factor': 60 },
    'sec_to_min': { 'from': 'sec', 'to': 'min', 'factor': 1/60 },
    'hr_to_sec': { 'from': 'hr', 'to': 'sec', 'factor': 3600 },
    'sec_to_hr': { 'from': 'sec', 'to': 'hr', 'factor': 1/3600 },
    'min_to_hr': { 'from': 'min', 'to': 'hr', 'factor': 1/60 },
    'hr_to_min': { 'from': 'hr', 'to': 'min', 'factor': 60 },

    # Weight
    'g_to_mg': { 'from': 'g', 'to': 'mg', 'factor': 1000 },
    'mg_to_g': { 'from': 'mg', 'to': 'g', 'factor': 0.001},
    'g_to_kg': { 'from': 'g', 'to': 'kg', 'factor': 0.001 },
    'kg_to_g': { 'from': 'kg', 'to': 'g', 'factor': 1000 },
}

desire_to_solve_unit_conversions = int(input("Enter the amount of unit conversion problems to solve for:\n> "))

# Loop for repeating problems
for i in range(desire_to_solve_unit_conversions):
    conversion_key = random.choice(list(conversions.keys()))
    conversion = conversions[conversion_key]

    if conversion['from'] in ['km','kg','hr']:
        value = round(random.uniform(1, 50.1),2)
    elif conversion['from'] in ['m','g','min','m/s']:
        value = round(random.uniform(1,500.1),2)
    elif conversion['from'] in ['cm','mm','mg','s','km/hr']:
        value = round(random.uniform(1,1000.1),2)
    else:
        value = round(random.uniform(1,100.1),2)

    # Take input and calculate answers
    conversion_user_input = float(input(f"Convert {value} {conversion['from']} to {conversion['to']}:\n> "))
    conversion_answer = value*conversion['factor']

    # Check answer and display if correct or not
    print(f"Correct! {conversion_answer:.2f}" if abs(conversion_user_input-conversion_answer) < 0.1 else f"Incorrect... {conversion_answer:.2f}")