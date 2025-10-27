import sys


def str_to_morse(input_str: str) -> str:
    """Takes a str as input and return its equivalent in morse code"""

    NESTED_MORSE = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',

        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',

        ' ': '/'
    }

    morse_str = " ".join(NESTED_MORSE[c.upper()] for c in input_str)

    return morse_str


def main():
    assert len(sys.argv) == 2, "the arguments are bad"

    assert isinstance(sys.argv[1], str), "the arguments are bad"

    input_str = sys.argv[1]

    assert all(
        char.isalnum() or char.isspace()
        for char in input_str
    ), "the arguments are bad"

    print(str_to_morse(input_str))


if __name__ == "__main__":
    try:
        main()

    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)
