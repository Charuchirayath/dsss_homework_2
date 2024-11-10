import random

def integer_generator(min_num, max_num):
    """
    Generate a random integer between min and max.
    Parameters:
        min_num (int): The minimum value the random integer can be.
        max_num (int): The maximum value the random integer can be.
    Returns:
        rand_int(int): A random integer between min and max.
    """
    return random.randint(min_num, max_num)

def operator_generator():
    """
    Generate a random operator from '+', '-', and '*'.
    
    Returns:
        operator (str): A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])

def problem_generator(n1, n2, oper):
    """
    Generate a mathematical problem and its solution.

    Parameters:
        n1 (int): The first number in the problem.
        n2 (int): The second number in the problem.
        oper (str): The operator to use for the operation.

    Returns:
        eqn (tuple): A tuple containing the problem as a string and the correct
        answer.
    """
    prob = f"{n1} {oper} {n2}"
    if oper == '+': ans = n1 + n2
    elif oper == '-': ans = n1 - n2
    else: ans = n1 * n2
    return prob, ans

def math_quiz():
    """
    Main function to run the math quiz game.
    
    The game will present a series of math problems and ask the user to solve them.
    The user's score will be calculated based on correct answers.
    """
    score = 0
    tot_qn = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(tot_qn):
        n1 = integer_generator(1, 10)
        n2 = integer_generator(1, 5)
        oper = operator_generator()

        prob, correct_answer = problem_generator(n1, n2, oper)
        print(f"\nQuestion: {prob}")
         # Error handling for user input
        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        # Check the answer and update the score
        if useranswer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
    
    # Display the final score
    print(f"\nGame over! Your score is: {score}/{tot_qn}")

if __name__ == "__main__":
    math_quiz()