import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        input_str = sys.argv[1]

        if input_str.isdigit():
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
