from array2D import slice_me

# Valid values
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print("Valid values")
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# # Wrong arguments type
# print("\n<family> is str instead of list")
# print(slice_me("Family", 0, 2))
# print("\n<start> is float instead of int")
# print(slice_me(family, 0.5, 2))
# print("\n<end> is str instead of int")
# print(slice_me(family, 0, "string"))

# # Uneven family argument
# family = [[1.80, 78.4],
#           [2.15, 102.7],
#           [2.10],
#           [1.88, 75.2]]
# print("\nUneven family argument")
# print(slice_me(family, 0, 2))
