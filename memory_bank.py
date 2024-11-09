# Memory Bank Feature

# Dictionary to store problems
memory_bank = {}

def add_problem(question, answer):
    memory_bank[question] = answer
    print("Problem added to Memory Bank.")

def view_problems():
    for question, answer in memory_bank.items():
        print(f"Question: {question}, Answer: {answer}")

# Example usage
add_problem("What is 5 + 3?", 8)
add_problem("What is 10 - 4?", 6)

print("Memory Bank Contents:")
view_problems()
