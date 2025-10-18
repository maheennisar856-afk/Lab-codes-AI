def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Stored correct credentials
    correct_username = "admin"
    correct_password = "12345"

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

# Example usage
login_system()
