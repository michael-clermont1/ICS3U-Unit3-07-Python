#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a guessing game


def main():
    # this function shows formatting output

    # input
    age_as_string = input("Please enter your age: ")
    # process & output
    print("")
    try:
        age_as_int = int(age_as_string)
        if age_as_int > 25 and age_as_int < 40:
            print("You are an acceptable age.")
        else:
            print("You are not an acceptable age.")
    except Exception:
        print("That is not an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
