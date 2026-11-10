# CTE213 PYTHON MINI PROJECT
# Project: Mechatronics Quiz App
# Author: OLOWOOKERE ADEWUNMI EMMANUEL
# Department: Mechatronics Engineering, YabaTech

# A list containing the quiz questions and their answers.
questions = [
    {
        "question": "What is the main function of a sensor?",
        "options": ["A. To detect changes", "B. To produce electricity",
                    "C. To store data", "D. To generate heat"],
        "answer": "A",
        "explanation": "A sensor detects changes in the environment and sends information to a system."
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Computer Processing Utility",
                    "B. Central Processing Unit",
                    "C. Control Power Unit",
                    "D. Central Program Utility"],
        "answer": "B",
        "explanation": "CPU means Central Processing Unit. It processes instructions in a computer."
    },
    {
        "question": "Which component converts electrical energy into motion?",
        "options": ["A. Resistor", "B. Capacitor",
                    "C. Electric motor", "D. Diode"],
        "answer": "C",
        "explanation": "An electric motor converts electrical energy into mechanical motion."
    },
    {
        "question": "What is the full meaning of PLC?",
        "options": ["A. Power Line Control",
                    "B. Programmable Logic Controller",
                    "C. Program Level Computer",
                    "D. Primary Logic Circuit"],
        "answer": "B",
        "explanation": "PLC means Programmable Logic Controller. It is used for industrial automation."
    },
    {
        "question": "Which of these is an actuator?",
        "options": ["A. Temperature sensor", "B. Light sensor",
                    "C. Electric motor", "D. Thermistor"],
        "answer": "C",
        "explanation": "An electric motor is an actuator because it produces movement."
    },
    {
        "question": "Which system combines mechanical and electronic engineering?",
        "options": ["A. Hydraulic system", "B. Mechatronic system",
                    "C. Manual system", "D. Cooling system"],
        "answer": "B",
        "explanation": "Mechatronics combines mechanical, electronic and computer control systems."
    },
    {
        "question": "What is the function of a resistor?",
        "options": ["A. To oppose electric current",
                    "B. To produce movement",
                    "C. To measure temperature",
                    "D. To store mechanical energy"],
        "answer": "A",
        "explanation": "A resistor opposes the flow of electric current."
    },
    {
        "question": "Which device is used to measure temperature?",
        "options": ["A. Motor", "B. Thermistor",
                    "C. Relay", "D. Switch"],
        "answer": "B",
        "explanation": "A thermistor is a temperature-sensitive resistor."
    }
]


# Function to collect and validate the user's answer.
def get_answer():
    while True:
        answer = input("Enter your answer (A-D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid answer. Please enter A, B, C or D.")


# Function to calculate the percentage score.
def calculate_percentage(score, total):
    if total == 0:
        return 0
    return (score / total) * 100


# Function to determine the student's grade.
def get_grade(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Very Good"
    elif percentage >= 50:
        return "Good"
    else:
        return "Needs Improvement"


# Function to ask the quiz questions.
def start_quiz():
    score = 0
    wrong_answers = []

    print("\n================================")
    print("       MECHATRONICS QUIZ")
    print("================================")

    print("\nWelcome to the Mechatronics Quiz App!")

    # Ask how many questions the user wants to attempt.
    while True:
        try:
            total_questions = int(
                input(f"\nChoose number of questions (1-{len(questions)}): ")
            )

            if 1 <= total_questions <= len(questions):
                break
            else:
                print("Please choose a number within the available range.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Display the selected questions one after another.
    for number, item in enumerate(questions[:total_questions], start=1):

        print(f"\nQuestion {number}: {item['question']}")

        for option in item["options"]:
            print(option)

        user_answer = get_answer()

        if user_answer == item["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            wrong_answers.append(item)
            print("Correct answer:", item["answer"])

    # Calculate and display the final result.
    percentage = calculate_percentage(score, total_questions)
    grade = get_grade(percentage)

    print("\n================================")
    print("          QUIZ RESULT")
    print("================================")

    print("Total questions:", total_questions)
    print("Correct answers:", score)
    print("Wrong answers:", total_questions - score)
    print(f"Percentage: {percentage:.1f}%")
    print("Grade:", grade)

    # ORIGINAL FEATURE: SMART REVISION MODE
    # The user can review and retry questions answered incorrectly.
    if wrong_answers:

        print("\n================================")
        print("       SMART REVISION MODE")
        print("================================")

        print("Let's review the questions you missed.")

        for item in wrong_answers:
            print("\nQuestion:", item["question"])
            print("Correct answer:", item["answer"])
            print("Explanation:", item["explanation"])

        print("\nWould you like to retry your missed questions?")
        retry = input("Enter Y for Yes or N for No: ").strip().upper()

        if retry == "Y":
            retry_score = 0

            for item in wrong_answers:
                print("\n", item["question"])

                for option in item["options"]:
                    print(option)

                answer = get_answer()

                if answer == item["answer"]:
                    print("Correct! You have improved.")
                    retry_score += 1
                else:
                    print("Not quite. The correct answer is", item["answer"])

            # Display improvement after revision.
            print("\nREVISION RESULT")
            print("Questions retried:", len(wrong_answers))
            print("Correct on retry:", retry_score)

            retry_percentage = calculate_percentage(
                retry_score, len(wrong_answers)
            )

            print(f"Revision percentage: {retry_percentage:.1f}%")

        elif retry == "N":
            print("You can practise again anytime.")

        else:
            print("Invalid selection. Revision skipped.")

    else:
        print("\nPerfect score! You got every question correct.")

    print("\nThank you for using the Mechatronics Quiz App!")


# Main program: start the quiz.
if __name__ == "__main__":
    start_quiz()