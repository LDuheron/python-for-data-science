from give_bmi import give_bmi, apply_limit

print(give_bmi.__doc__)
print(apply_limit.__doc__)
# # Valid values
# height = [2.71, 1.15]
# weight = [165.3, 38.4]

# bmi = give_bmi(height, weight)
# print("Valid values")
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))

# # ZeroDivisionError
# height = [2.71, 0]
# weight = [165.3, 38.4]

# print("\nZeroDivisionError")
# bmi = give_bmi(height, weight)

# # Different lenghts error
# height = [2.71]
# weight = [165.3, 38.4]

# print("\nDifferent len lists")
# bmi = give_bmi(height, weight)

# # String in list
# height = [2.71, "a"]
# weight = [165.3, 38.4]

# print("\nString in list error")
# bmi = give_bmi(height, weight)
