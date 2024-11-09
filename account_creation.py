# Simple Account Creation Starter Code

def create_account(username, password):
    # Basic function to store account info (for now, just print it)
    print("Account created!")
    print(f"Username: {username}")
    # For security, avoid printing the password in real code
    return {"username": username, "password": password}

# Example usage
user_account = create_account("new_user", "password123")
