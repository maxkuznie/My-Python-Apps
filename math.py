import random

def math_game():
    score = 0
    while True:
        # Generate two random numbers
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        
        # Calculate correct answer
        if operator == '+': answer = num1 + num2
        elif operator == '-': answer = num1 - num2
        else: answer = num1 * num2
        
        # Get user input
        user_guess = int(input(f"What is {num1} {operator} {num2}? "))
        
        # Check answer
        if user_guess == answer:
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Wrong! Final Score: {score}")
            break

# Uncomment to run the game
# math_game()
