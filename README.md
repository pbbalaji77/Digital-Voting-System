# Digital Voting System

A simple beginner-friendly Digital Voting System developed using Python.

## Project Description

This project is a console-based voting application that allows registered voters to cast their vote for a candidate.

The system automatically identifies the voter using their Voter ID and prevents the same voter from voting more than once.

## Features

- Add a new voter
- Display registered voters
- Display candidates
- Search voter using Voter ID
- Automatically display voter name
- Cast a vote
- Prevent duplicate voting
- Display voting results
- Simple menu-driven interface

## Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- User Input

## Candidates

The demo application contains three sample candidates:

- Modi ji
- Rahul ji
- Thalapathy

## Sample Voters

The project includes sample voters for demonstration:

| Voter ID | Name |
|----------|------|
| V001 | Dhoni |
| V002 | Sachin |
| V003 | Virat |

## How to Run

### 1. Clone the repository

`bash
git clone https://github.com/pbbalaji77/Digital-Voting-System.git

Step 2: Select an Option
The program displays:
===== DIGITAL VOTING SYSTEM =====

1. Add Voter
2. Display Voters
3. Display Candidates
4. Cast Vote
5. Show Results
6. Exit

Enter your choice:


Step 3: Enter Voter ID

When the voter selects the voting option:
===== CAST VOTE =====

Enter Voter ID: V001
The system automatically finds the voter:
Voter Name: Dhoni
The voter does not need to enter their name separately.
Step 4: Select a Candidate
The system displays:
===== CANDIDATES =====

C001 - Narendra Modi
C002 - Rahul Gandhi
C003 - Thalapathy Vijay
The voter enters the Candidate ID.
Example:
Enter Candidate ID: C003
The vote is then recorded.
Vote cast successfully.
Duplicate Voting Prevention
After a voter casts their vote, their voting status is changed from:
False

to:
True
If the same voter tries to vote again, the system displays:
You have already voted.
Invalid Voter ID
If a voter enters an ID that does not exist:
Enter Voter ID: V999
The system displays:
Voter not found.
Invalid Candidate ID
If an invalid candidate ID is entered:
Enter Candidate ID: C999
The system displays:
Candidate not found.
Voting Results
The results option displays the number of votes received by each candidate.
Example:
===== VOTING RESULTS =====

Narendra Modi - 1 votes
Rahul Gandhi - 0 votes
Thalapathy Vijay - 2 votes
Project Structure
Digital-Voting-System/
│
├── voting_system.py
└── README.md
Main Python Concepts Used
1. Lists
Lists are used to store voters and candidates.
voters = []
candidates = []
2. Dictionaries
Each voter and candidate is represented using a dictionary.
Example:
{
    "voter_id": "V001",
    "name": "Dhoni",
    "voted": False
}
3. Functions
Different functions are used for different operations.
add_voter()
display_voters()
display_candidates()
cast_vote()
show_results()
main()
4. Loops
Loops are used to search voters and candidates and display information.
5. Conditional Statements
if, elif, and else are used for menu selection and validation.
6. User Input
The input() function is used to get information from the user.
Learning Outcomes
Through this project, I practiced:
Python programming fundamentals
Lists and dictionaries
Functions and modular programming
for loops
if-elif-else conditions
Searching data
Updating dictionary values
User input validation
Menu-driven applications
Basic project structure
Git and GitHub
Limitations
This project is designed as a Python learning/demo project and is not intended to be used as a real-world election system.
The voter and candidate information is stored only in Python memory, so the data is reset when the program is restarted.
Future Improvements
The project can be improved by adding:
SQLite or MySQL database
User authentication
Admin login
Password or PIN verification
Graphical User Interface (GUI)
Web-based interface
Persistent voter records
Voting reports
Result visualization
Better security and validation
How to Run
Requirements
Python 3.x
VS Code or any Python-supported IDE
Run the Project
Open the project folder in the terminal:
cd Digital-Voting-System
Run:
python voting_system.py
For Windows, you can also use:
py voting_system.py
GitHub Repository
Digital Voting System
https://github.com/pbbalaji77/Digital-Voting-System⁠�
Author
Balaji P B
GitHub:
https://github.com/pbbalaji77⁠�