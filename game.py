# DOPISAC KOD NA OSZUKIWANIE
print("Think of a number from 0 to 1000, and I'll guess it in max. 10 attempts")


def computer_guess():
    min_num = 0
    max_num = 1000
    attempts = 0

    while attempts < 10:
        guess = int(((max_num - min_num) / 2) + min_num)
        print(f"I'm guessing: {guess}. Is it correct?")

        user_response = input('Enter "yes" if correct, "too much" if computer num > user num, "not enough" if computer num < user num: ')

        if user_response == "yes":
            print("I won!")
            break
        elif user_response == "too much":
            max_num = guess - 1
        elif user_response == "not enough":
            min_num = guess + 1
        else:
            print("Invalid input. Please enter 'yes', 'too much', or 'not enough.")

        attempts += 1

    if attempts == 10:
        print("I couldn't guess the number in 10 attempts. You win!")


# Wywołanie funkcji
computer_guess()
