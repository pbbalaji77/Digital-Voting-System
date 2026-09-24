voters = [
    {"voter_id": "V001", "name": "Dhoni", "voted": False},
    {"voter_id": "V002", "name": "Sachin", "voted": False},
    {"voter_id": "V003", "name": "Virat", "voted": False}
]

candidates = [
    {"candidate_id": "C001", "name": "Modi ji", "votes": 0},
    {"candidate_id": "C002", "name": "Rahul ji", "votes": 0},
    {"candidate_id": "C003", "name": "Thalapathy", "votes": 0}
]


def add_voter():
    print("\n===== ADD VOTER =====")

    voter_id = input("Enter Voter ID: ")
    name = input("Enter Voter Name: ")

    for voter in voters:
        if voter["voter_id"] == voter_id:
            print("Voter ID already exists.")
            return

    voters.append({
        "voter_id": voter_id,
        "name": name,
        "voted": False
    })

    print("Voter added successfully.")


def display_voters():
    print("\n===== VOTERS =====")

    if len(voters) == 0:
        print("No voters found.")
        return

    for voter in voters:
        print(voter["voter_id"], "-", voter["name"])


def display_candidates():
    print("\n===== CANDIDATES =====")

    for candidate in candidates:
        print(
            candidate["candidate_id"],
            "-",
            candidate["name"]
        )


def cast_vote():
    print("\n===== CAST VOTE =====")

    voter_id = input("Enter Voter ID: ")

    voter_found = False

    for voter in voters:
        if voter["voter_id"] == voter_id:
            voter_found = True

            print("Voter Name:", voter["name"])

            if voter["voted"]:
                print("You have already voted.")
                return

            break

    if not voter_found:
        print("Voter ID not found.")
        return

    display_candidates()

    candidate_id = input("Enter Candidate ID: ")

    candidate_found = False

    for candidate in candidates:
        if candidate["candidate_id"] == candidate_id:
            candidate["votes"] += 1
            candidate_found = True
            break

    if not candidate_found:
        print("Candidate ID not found.")
        return

    for voter in voters:
        if voter["voter_id"] == voter_id:
            voter["voted"] = True

    print("Vote cast successfully.")


def show_results():
    print("\n===== VOTING RESULTS =====")

    for candidate in candidates:
        print(
            candidate["name"],
            "-",
            candidate["votes"],
            "votes"
        )


def main():

    while True:

        print("\n===== DIGITAL VOTING SYSTEM =====")
        print("1. Add Voter")
        print("2. Display Voters")
        print("3. Display Candidates")
        print("4. Cast Vote")
        print("5. Show Results")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_voter()

        elif choice == "2":
            display_voters()

        elif choice == "3":
            display_candidates()

        elif choice == "4":
            cast_vote()

        elif choice == "5":
            show_results()

        elif choice == "6":
            print("Thank you for using the Digital Voting System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()