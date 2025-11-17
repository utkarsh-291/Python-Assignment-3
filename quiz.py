# Name: Utkarsh Gupte
# Enrollment No.: 0103CS231441
# Batch: BATCH 6 (Mtf)
# Batch Time: 12:10 pm - 1:50 pm

import json
import random
import datetime

RESULTS_FILE = 'results.json'

def loadQuestions():
    questions = {
        "Dsa": [
            {
                "que": "What is the time complexity of binary search?",
                "options": ["A: O(n)", "B: O(log n)", "C: O(n^2)", "D: O(1)"],
                "answer": "B"
            },
            {
                "que": "Which data structure uses LIFO (Last-In, First-Out)?",
                "options": ["A: Queue", "B: Array", "C: Stack", "D: Linked List"],
                "answer": "C"
            },
            {
                "que": "What is a 'greedy algorithm'?",
                "options": ["A: An algorithm that finds the optimal solution at each step.", "B: An algorithm that explores all possible solutions.", "C: An algorithm that uses dynamic programming.", "D: An algorithm that works backwards."],
                "answer": "A"
            },
            {
                "que": "Which sorting algorithm has a worst-case time complexity of O(n^2)?",
                "options": ["A: Merge Sort", "B: Quicksort", "C: Heap Sort", "D: Timsort"],
                "answer": "B"
            },
            {
                "que": "What does 'FIFO' stand for?",
                "options": ["A: First-In, First-Out", "B: Fast-In, Fast-Out", "C: First-In, Fast-Out", "D: Final-In, First-Out"],
                "answer": "A"
            }
        ],
        "Dbms": [
            {
                "que": "What does SQL stand for?",
                "options": ["A: Strong Question Language", "B: Structured Query Language", "C: Simple Query Language", "D: Server Query Language"],
                "answer": "B"
            },
            {
                "que": "Which command is used to retrieve data from a database?",
                "options": ["A: GET", "B: FETCH", "C: RETRIEVE", "D: SELECT"],
                "answer": "D"
            },
            {
                "que": "What is a 'Primary Key'?",
                "options": ["A: A key to open the database.", "B: The first key added to a table.", "C: A unique identifier for a record in a table.", "D: A foreign key from another table."],
                "answer": "C"
            },
            {
                "que": "Which type of JOIN returns all rows from the left table, and the matched rows from the right table?",
                "options": ["A: INNER JOIN", "B: RIGHT JOIN", "C: FULL JOIN", "D: LEFT JOIN"],
                "answer": "D"
            },
            {
                "que": "What command is used to add a new row to a table?",
                "options": ["A: ADD", "B: CREATE", "C: INSERT INTO", "D: NEW ROW"],
                "answer": "C"
            }
        ],
        "Python": [
            {
                "que": "What does 'print()' do?",
                "options": ["A: Takes user input", "B: Displays output to the console", "C: Defines a variable", "D: Runs a loop"],
                "answer": "B"
            },
            {
                "que": "Which keyword is used to define a function in Python?",
                "options": ["A: func", "B: function", "C: def", "D: define"],
                "answer": "C"
            },
            {
                "que": "What is the correct way to create a list in Python?",
                "options": ["A: (1, 2, 3)", "B: {1, 2, 3}", "C: [1, 2, 3]", "D: <1, 2, 3>"],
                "answer": "C"
            },
            {
                "que": "How do you check the data type of a variable 'x'?",
                "options": ["A: type(x)", "B: typeof(x)", "C: x.type", "D: datatype(x)"],
                "answer": "A"
            },
            {
                "que": "Which operator is used for exponentiation?",
                "options": ["A: ^", "B: *", "C: %", "D: **"],
                "answer": "D"
            }
        ]
    }
    return questions

def loadResults():
    try:
        with open(RESULTS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("can't fetch results")
        return []

def saveResults(results):
    with open(RESULTS_FILE, 'w') as f:
        json.dump(results, f, indent=4)

def attemptQuiz(currentUser):
    all_questions = loadQuestions()
    
    print()
    print("--- Select Quiz Category ---")
    print("1. Dsa")
    print("2. Dbms")
    print("3. Python")
    
    chosen_category = ""
    
    choice = input("Enter your choice: 1/2/3: ")
    if choice == '1':
        chosen_category = "Dsa"
    elif choice == '2':
        chosen_category = "Dbms"
    elif choice == '3':
        chosen_category = "Python"
    else:
        print("Invalid choice. Please try again...")
        return
    questions_to_ask = all_questions[chosen_category]
    
    random.shuffle(questions_to_ask)
    
    score = 0
    total_questions = len(questions_to_ask)
    
    print()
    print(f"--- {chosen_category} Quiz ---")
    
    for i, q in enumerate(questions_to_ask):
        print()
        print(f"Question {i+1}: {q['que']}")
        for opt in q['options']:
            print(f"  {opt}")
            
        answer = input("Your answer: ").upper()
        if answer == q['answer']:
            score += 1
            
    print()
    print("--- Quiz Finished ---")
    print(f"Your final score is: {score}/{total_questions}")
    
    time = datetime.datetime.now().isoformat()
    
    results = loadResults()
    results.append({
        "enrollment": currentUser,
        "category": chosen_category,
        "correct": score,
        "total": total_questions,
        "datetime": time
    })
    saveResults(results)