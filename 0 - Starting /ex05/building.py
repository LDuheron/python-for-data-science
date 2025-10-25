import sys


def count_characters(input_str: str):
    """Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters, digits
    and spaces."""
    counts = {
        'upper': 0,
        'lower': 0,
        'digit': 0,
        'space': 0,
        'punctuation': 0
    }

    for c in input_str:
        if c.isupper():
            counts['upper'] += 1
        elif c.islower():
            counts['lower'] += 1
        elif c.isdigit():
            counts['digit'] += 1
        elif c.isspace():
            counts['space'] += 1
        else:
            counts['punctuation'] += 1

    text = (
        f"The text contains {len(input_str)} characters:\n"
        f"{counts['upper']} upper letters\n"
        f"{counts['lower']} lower letters\n"
        f"{counts['punctuation']} punctuation marks\n"
        f"{counts['space']} spaces\n"
        f"{counts['digit']} digits"
    )

    print(text)


def main():
    argument_count = len(sys.argv)

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if argument_count == 1:
            user_input = input("What is the text to count?\n")
        else:
            user_input = sys.argv[1]

        count_characters(user_input)

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)


if __name__ == "__main__":
    main()
