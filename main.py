def count_letters(text: str) -> dict:
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def print_report(text: str):
    letter_counts = count_letters(text)
    print("------Begin Report-------")
    for character, count in letter_counts.items():
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")
    print("------End Report-------")


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        # print(contents)
        # print(count_words(contents))
        # print(count_letters(contents))
        print_report(contents)


if __name__ == "__main__":
    main()
