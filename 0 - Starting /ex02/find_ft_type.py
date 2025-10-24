def all_thing_is_obj(object: any) -> int:
	"""Prints the object types and returns 42"""
	obj_type = type(object)
	print(f'{obj_type.__name__.capitalize()} : {obj_type}')
	return 42