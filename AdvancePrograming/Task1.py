import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(0, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ")
    return int(input())

def isCorrect(user_answer, correct_answer, num1, num2, operation):
    if user_answer == correct_answer:
        print("Correct!")
        return 10
    else:
        print("Incorrect, Try again.")
        second_attempt = int(input(f"{num1} {operation} {num2} = "))
        if second_attempt == correct_answer:
            print("Correct on second attempt.")
            return 5
        else:
            print("Incorrect.")
            return 0

def displayResults(score):
    print(f"Your final score is: {score}/100")
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: F")

def main():
    while True:
        displayMenu()
        difficulty = int(input("Enter difficulty level (1, 2, or 3): "))

        score = 0
        for _ in range(10):
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()

            user_answer = displayProblem(num1, num2, operation)
            correct_answer = eval(f"{num1}{operation}{num2}")
            score += isCorrect(user_answer, correct_answer, num1, num2, operation)

        displayResults(score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()