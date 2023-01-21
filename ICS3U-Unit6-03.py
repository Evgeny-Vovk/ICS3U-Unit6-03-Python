# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: January 2022
# ICS3U-Unit6-03.py File, learning functions with parameters in python.

import random


def smallest_number(random_numbers):
    answer = 100
    for number in random_numbers:
        if answer > number:
            answer = number
    return answer


def main():

    random_numbers = []

    for counter in range(10):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("Generated number: {0}".format(number))

    answer = smallest_number(random_numbers)

    print("\nThe smallest number of all numbers is {0}.".format(answer))
    print("")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
