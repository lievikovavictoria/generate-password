# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import string


def main():
    # characters to form a password
    letters = string.ascii_letters
    numbers = '0123456789'
    symbols = '#@$%&*-=+/.'

    # group all characters
    chars = letters + numbers + symbols

    # define a password length
    password_length = int(input('Enter a password length: '))

    # generate a password
    password = "".join(random.sample(chars, password_length))

    print(password)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
