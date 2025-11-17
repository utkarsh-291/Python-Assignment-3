# Name: Utkarsh Gupte
# Enrollment No.: 0103CS231441
# Batch: BATCH 6 (Mtf)
# Batch Time: 12:10 pm - 1:50 pm

import json

USERS_FILE = 'users.json'

def initFiles():
    try:
        with open(USERS_FILE, 'x') as f:
            adminUser = {
                "admin": {
                    "name": "Admin",
                    "password": "adminHoon567"
                }
            }
            json.dump(adminUser, f, indent=4)
    except FileExistsError:
        pass

def loadUsers():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def saveUsers(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def registerUser():
    print()
    print("--- User Registration ---")
    users = loadUsers()
    
    while True:
        enrollment = input("Enter enrollment: ")
        if not enrollment:
            print("Enrollment cannot be blank.")
        elif enrollment in users:
            print("Enrollment already exists. Please try another.")
        else:
            break
            
    password = input("Enter password (min 8 chars): ")
    while len(password) < 8:
        password = input("Password too short. Enter password (min 8 chars): ")
        
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    
    print()
    print("--- Security Question ---")
    securityQ = input("Enter a security question ")
    while not securityQ: 
        securityQ = input("Question cannot be empty as it has to be used in case of forgetting password ")
    
    securityA = input(f"Answer for: {securityQ}")
    while not securityA:
        securityA = input(f"Answer cannot be blank. {securityQ} ")

    users[enrollment] = {
        "name": name,
        "password": password,
        "email": email,
        "phone": phone,
        "security_q": securityQ,
        "security_a": securityA
    }
    
    saveUsers(users)
    print()
    print("Registration successful!")

def loginUser(): 
    print()
    print("--- User Login ---")
    users = loadUsers()
    
    enrollment = input("Enter enrollment: ")
    password = input("Enter password: ")
    
    if enrollment in users and users[enrollment]['password'] == password:
        print()
        print(f"Welcome back, {users[enrollment]['name']}!")
        
        return enrollment
    else:
        print()
        print("Invalid enrollment or password.")
        return None

def forgotPassword():
    print()
    print("--- Reset Password ---")
    users = loadUsers()
    
    enrollment = input("Enter your enrollment: ")
    if enrollment not in users:
        print("Enrollment not found.")
        return
        
    if enrollment == 'admin':
        print("Admin password cannot be reset.")
        return

    details = users[enrollment]
    print()
    print(f"Security Question: {details['security_q']}")
    answer = input("Enter your answer: ")
    
    if answer.lower() == details['security_a'].lower():
        print()
        print(f"Your password is: {details['password']}")
    else:
        print()
        print("Incorrect answer.")