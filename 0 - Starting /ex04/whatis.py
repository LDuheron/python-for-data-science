import sys

argument_count = len(sys.argv)

if argument_count == 1:
    sys.exit(0)

try:
    assert argument_count == 2, "more than one argument is provided"

    user_input = int(sys.argv[1])

    if user_input % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except ValueError:
    print("ValueError: argument is not an integer")
    sys.exit(1)

except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)

except Exception as error:
    print(f"AssertionError: {error}")
    sys.exit(1)
