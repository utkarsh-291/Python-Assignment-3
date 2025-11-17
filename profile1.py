# Name: Utkarsh Gupte
# Enrollment No.: 0103CS231441
# Batch: BATCH 6 (Mtf)
# Batch Time: 12:10 pm - 1:50 pm

import auth

def showProfile(currentUser):
    users = auth.loadUsers()
    details = users[currentUser]
    
    print()
    print("--- Your Profile ---")
    print(f"Enrollment: {currentUser}")
    print(f"Name: {details['name']}")
    print(f"Email: {details['email']}")
    print(f"Phone: {details['phone']}")

def updateProfile(currentUser):
    users = auth.loadUsers()
    details = users[currentUser]
    
    print()
    print("--- Update Profile ---")
    print("Leave blank for no changes.")
   
    newName = input(f"Name ({details['name']}): ")
    newEmail = input(f"Email ({details['email']}): ")
    newPhone = input(f"Phone ({details['phone']}): ")
    
    if newName:
        details['name'] = newName
    if newEmail:
        details['email'] = newEmail
    if newPhone:
        details['phone'] = newPhone      
    users[currentUser] = details
    auth.saveUsers(users)
    
    print()
    print("Profile updated successfully!")

def changePassword(currentUser):
    users = auth.loadUsers()
    details = users[currentUser]
    
    print()
    print("--- Change Password ---")
    oldPassword = input("Enter your old password: ")
    
    if oldPassword != details['password']:
        print("Incorrect old password.")
        return
        
    newPassword = input("Enter new password (min 8 chars): ")
    while len(newPassword) < 8:
        newPassword = input("Password too short. Enter new password (min 8 chars): ")
        
    details['password'] = newPassword
    users[currentUser] = details
    auth.saveUsers(users)
    
    print("Password changed successfully!")