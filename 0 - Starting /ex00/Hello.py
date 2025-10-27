ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modify ft_list
ft_list.pop()
ft_list.append("World!")

# Overwrite ft_tuple
ft_tuple = ("Hello", "France!")

# Modify ft_set
ft_set.discard("tutu!")
ft_set.add('Paris!')

# Modify ft_dict["Hello"]
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
