def is_palindrome(text):
    text = text.lower()

    return text == text[::-1]


def count_words(text):
    words = text.split(" ")
    return len(words)


def reverse_text(text):
    if not text:
        return None

    return text[::-1]


def normalize_text(text):
    return text.strip()


if __name__ == "__main__":
    text = input("Enter a sentence: ")

    print("Palindrome:", is_palindrome(text))
    print("Word count:", count_words(text))
    print("Reversed:", reverse_text(text))