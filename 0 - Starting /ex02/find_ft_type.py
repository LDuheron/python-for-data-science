def all_thing_is_obj(object: any) -> int:
	"""Prints the object types and returns 42"""
	obj_type = type(object)

	if isinstance(object, (list, dict, tuple, set)):
		print(f'{obj_type.__name__.capitalize()} : {obj_type}')
	elif isinstance(object, str):
		print(f'{object} is in the kitchen : {obj_type}')
	else:
		print("Type not Found")

	return 42