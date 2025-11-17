# Assignment 3 - 

## Project Info
* **Name:** Utkarsh Gupte
* **Enrollment:** 0103CS231441
* **Batch:** BATCH 6 (Mtf)

## Key Features

### Authentication Module
* **Registration:** Users can sign up with enrollment number, password, and personal details.
* **Security:** Includes password strength validation (min 8 chars) and Security Questions for password recovery.
* **Login:** Secure login system for both Students and Admins.
* **Forgot Password:** Recovery mechanism using the security question answer.

### Student Module
* **Profile Management:** View and update personal details (Name, Email, Phone).
* **Change Password:** Securely update login credentials.
* **Take Quiz:** Attempt quizzes in three categories:
    * DSA (Data Structures & Algorithms)
    * DBMS (Database Management Systems)
    * Python Programming
* **Scoring:** Instant score calculation and result saving.

### Admin Module
* **View Users:** List all registered students.
* **View Results:** Track performance and scores of all students.
* **View Questions:** Review the question bank for all categories.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Storage:** JSON (File Handling) for storage of users and results.
* **Libraries:** `json`, `random`, `datetime`.

## How to Run

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/your-username/repository-name.git](https://github.com/your-username/repository-name.git)
    ```

2.  **Navigate to the directory:**
    ```bash
    cd repository-name
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```
    
To access the Admin Dashboard, use the following credentials:
* **Enrollment:** `admin`
* **Password:** `adminHoon567`
