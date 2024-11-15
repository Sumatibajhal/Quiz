import random

def registration():
    name = input("Enter your name: ")
    password = input("Create a password: ")
    roll_number = input("Enter your roll number: ")
    section = input("Enter your section: ")
    
    with open("users.txt", "a") as file:
        file.write(f"{roll_number},{password},{name},{section}\n")
    print("Registration successful!")

def login():
    roll_number = input("Enter your roll number: ")
    password = input("Enter your password: ")
    
    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            user_data = user.strip().split(',')
            if user_data[0] == roll_number and user_data[1] == password:
                print("Login successful!")
                return roll_number
    print("Login failed!")
    return None

def load_questions(subject):
    with open(f"{subject}.txt", "r", encoding="utf-8") as file:
        questions = file.readlines()
    return random.sample(questions, 5)

def attempt_quiz(roll_number):
    subjects = ["dsa", "dbms", "python"]
    subject = input("Choose a subject (dsa, dbms, python): ")
    if subject not in subjects:
        print("Invalid subject!")
        return

    questions = load_questions(subject)
    score = 0
    for question in questions:
        parts = question.strip().split('|')
        q, options, a = parts[0], parts[1:4], parts[4]
        print(f"{q}")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        answer = input("Enter the correct option number: ")
        if options[int(answer) - 1].lower() == a.lower():
            score += 1

    with open("results.txt", "a") as file:
        file.write(f"{roll_number},{subject},{score}\n")
    print(f"Quiz finished! You scored {score}/5")

def show_results(roll_number):
    with open("results.txt", "r") as file:
        results = file.readlines()
        for result in results:
            result_data = result.strip().split(',')
            if result_data[0] == roll_number:
                print(f"Subject: {result_data[1]}, Score: {result_data[2]}")
                return True
    print("No quiz results found!")
    return False
                
def main():
    logged_in_roll_number = None
    quiz_attempted = False
    while True:
        print("\n1. Registration\n2. Login\n3. Attempt Quiz\n4. Show Results\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            registration()
        elif choice == 2:
            logged_in_roll_number = login()
            if logged_in_roll_number:
                print("\nWelcome to the Quiz Portal!")
        elif choice == 3:
            if logged_in_roll_number:
                attempt_quiz(logged_in_roll_number)
                quiz_attempted = True
            else:
                print("You must be logged in to attempt the quiz!")
        elif choice == 4:
            if logged_in_roll_number and quiz_attempted:
                show_results(logged_in_roll_number)
            else:
                print("You must log in and attempt the quiz before viewing results!")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
