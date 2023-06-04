import random


def lotto():
    """
    Function select six random numbers.
    User select his six numbers.
    Function check if selected numbers are the same.
    Function shows common numbers.
    """

    numbers = list(range(1, 50))
    random.shuffle(numbers)
    user_numbers = []

    while len(user_numbers) < 6:
        user_num = input("Enter number")
        if not user_num.isdigit():
            print("Wrong value. Enter number:")
            continue

        user_num = int(user_num)
        if user_num not in range(0, 50):
            print("Number out of range!")
            continue

        elif user_num in user_numbers:
            print("Numbers cannot be repeated! Select different numbers:")
            continue

        user_numbers.append(user_num)
    user_numbers.sort()
    print("Your numbers:", set(user_numbers))
    print("Winning numbers:", set(numbers[0:6]))
    win = set(numbers[0:6])
    common_numbers = win.intersection(set(user_numbers))
    print("Overlapping numbers:", common_numbers)
    print("Common numbers:", len(common_numbers))


lotto()
