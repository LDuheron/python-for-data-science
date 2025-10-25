import sys

try:
	if len(sys.argv) != 2:
		raise AssertionError("more than one argument provided")

	user_input = int(sys.argv[1])

	if user_input % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

except ValueError as error:
	print(f"AssertionError: argument is not an integer")

except Exception as error:
	print(f"AssertionError: {error}") 