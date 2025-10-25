def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
     return the items that are true."""

    new_iterable = iter(iterable)
    if function is None:
        new_iterable = (x for x in iterable if x)
    else:
        new_iterable = (x for x in iterable if function(x))

    return new_iterable
