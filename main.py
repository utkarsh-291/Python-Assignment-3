# Name: Utkarsh Gupte
# Enrollment No.: 0103CS231441
# Batch: BATCH 6 (Mtf)
# Batch Time: 12:10 pm - 1:50 pm

#enter following cred. to login as admin
#admin enrollment - admin
#admin password - "adminHoon567"

import auth
import profile1
import quiz
import admin

def showUserMenu(currentUser):
    while True:
        print()
        print(f"{currentUser}")
        print("1. Profile")
        print("2. Update Profile")
        print("3. Change Password")
        print("4. Attempt Quiz")
        print("5. Logout")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            profile1.showProfile(currentUser)
        elif choice == '2':
            profile1.updateProfile(currentUser)
        elif choice == '3':
            profile1.changePassword(currentUser)
        elif choice == '4':
            quiz.attemptQuiz(currentUser)
        elif choice == '5':
            print()
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def showAdminMenu(currentUser):
    while True:
        print()
        print("--- Admin Menu ---")
        print("1. View All Questions")
        print("2. View All Users")
        print("3. View All Results")
        print("4. Logout")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            admin.viewAllQuestions()
        elif choice == '2':
            admin.viewAllUsers()
        elif choice == '3':
            admin.viewAllResults()
        elif choice == '4':
            print()
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    auth.initFiles()
    
    while True:
        print()
        print("--- Welcome to lnct ---")
        print("1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == '1':
            auth.registerUser()
        elif choice == '2':
            currentUser = auth.loginUser()
            if currentUser:
                if currentUser == 'admin':
                    showAdminMenu(currentUser)
                else:
                    showUserMenu(currentUser)
        elif choice == '3':
            auth.forgotPassword()
        elif choice == '4':
            print()
            print("Bye bye!")
            break
        else:
            print("Invalid choice, please try again.")
main()