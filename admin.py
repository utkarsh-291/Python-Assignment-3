# Name: Utkarsh Gupte
# Enrollment No.: 0103CS231441
# Batch: BATCH 6 (Mtf)
# Batch Time: 12:10 pm - 1:50 pm

import auth
import quiz

def viewAllQuestions():
    print()
    print("--- All Quiz Questions ---")
    all_questions = quiz.loadQuestions()
    
    for category, questions in all_questions.items():
        print()
        print(f"--- Category: {category} ---")
       
        for i, q in enumerate(questions):
            print()
            print(f"  Question {i+1}: {q['que']}")
            print(f"    Answer: {q['answer']}")

def viewAllUsers():
    print()
    print("--- All Users ---")
    users = auth.loadUsers()
    
    for enrollment, details in users.items():
        print()
        print(f"Enrollment: {enrollment}")
        print(f"  Name: {details['name']}")
        if enrollment != 'admin':
            print(f"  Email: {details['email']}")
            print(f"  Phone: {details['phone']}")

def viewAllResults():
    print()
    print("--- All Quiz Results ---")
    results = quiz.loadResults()
    if not results:
        print("No results found.")
        return
        
    for i, res in enumerate(results):
        print()
        print(f"Result {i+1}:")
        print(f"  Enrollment: {res['enrollment']}")
  
        print(f"  Category: {res['category']}")
        print(f"  Score: {res['correct']}/{res['total']}")
        print(f"  Date: {res['datetime']}")