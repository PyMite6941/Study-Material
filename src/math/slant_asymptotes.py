import random

def format_vertical_asymptote(coefficients):
    terms = []
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        power = degree - i
        if coeff == 0:
            continue
        sign = '+' if coeff > 0 and i != 0 else '-'
        if power == 0:
            terms.append(f"{sign}{coeff}")
        elif power == 1:
            terms.append(f"{sign}{coeff}x")
        else:
            terms.append(f"{sign}{coeff}x^{power}")
    return ' '.join(terms)

desire_to_solve_asymptote_questions = int(input("How many vertical asymptote questions would you like to solve?\n> "))

for i in range(desire_to_solve_asymptote_questions):
    # Define variables randomly
    numerator_degree = random.randint(1,3)
    denominator_degree = random.randint(1,3)

    # Display the practice problem
    print(f"Your rational function has a numerator degree of {numerator_degree} and a denominator degree of {denominator_degree}.")

    # Get and store user input
    vertical_asymptote_input = str(input("Does this function have a vertical asymptote? (yes or no)\n> ")).lower().strip()

    # Determine if vertical asymptote exists
    if denominator_degree > 0:
        has_vertical_asymptote = True
    else:
        has_vertical_asymptote = False

    # If vertical asymptotes exist then continue
    if has_vertical_asymptote and vertical_asymptote_input == 'yes':
        print("Correct!")
        numerator_terms = []
        for i in range(numerator_degree+1):
            numerator_terms.append[random.randint(-5,5)]

    # If no vertical asymptotes exist then continue
    elif not has_vertical_asymptote and vertical_asymptote_input == 'no':
        print("Correct!")

    # If wrong then continue
    else:
        print("Incorrect,...")