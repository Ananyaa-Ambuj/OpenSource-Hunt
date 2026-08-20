def is_palindrome(number):
    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


def main():
    number = int(input("Enter a number: "))

    if is_palindrome(number):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")


if __name__ == "__main__":
    main()