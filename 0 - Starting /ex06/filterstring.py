import sys
import string
from ft_filter import ft_filter


def main():
    """Checks arguments and calls filter"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        input_str = sys.argv[1]

        if input_str.isdigit():
            raise AssertionError("the arguments are bad")

        invisible_chars = {
            "\t", "\n", "\r", "\v", "\f",
            "\u00A0", "\u2000", "\u2001", "\u2002", "\u2003", "\u2004",
            "\u2006", "\u2007", "\u2008", "\u2009", "\u200A", "\u200B",
            "\u202F", "\u205F", "\u3000", "\uFEFF", "\u2005"
        }

		if any(char in string.punctuation or char in invisible_chars for char in input_str):
			raise AssertionError("the arguments are bad")

        input_number = int(sys.argv[2])

        words = input_str.split()

        result = ft_filter(lambda word: len(word) > input_number, words)
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
