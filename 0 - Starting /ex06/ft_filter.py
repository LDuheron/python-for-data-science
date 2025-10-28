def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    new_iterable = iter(iterable)
    if function is None:
        new_iterable = [item for item in iterable if item]
    else:
        new_iterable = [item for item in iterable if function(item)]

    return new_iterable
