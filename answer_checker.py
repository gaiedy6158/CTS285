# Answer Checker Function
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return "Correct! Well done."
    else:
        return "Incorrect. Try again."

# Example Usage
# Let's say the correct answer to the problem is 42
correct_answer = 42

# Simulating user input
user_answer = int(input("What is your answer? "))

# Checking the answer
result = check_answer(user_answer, correct_answer)
print(result)
