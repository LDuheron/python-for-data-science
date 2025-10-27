import time


def print_loading_bar(percent: float, total: int):
    """Display a progress bar in the terminal with the percentage
    completed and the count of elements processed.

    Args:
        percent (float): Progress as a float between 0.0 and 1.0
        total (int): Total number of elements to process
    """
    bar_len = 70
    bar = int((percent * bar_len))
    blank = bar_len - bar
    bar_str = "=" * bar + ">" + " " * blank
    text = (
        f"\r{int(percent * 100):3d}%| "
        f"[{bar_str}] | {int(percent * total)}/{total}"
    )
    print(text, end="", flush=True)
    time.sleep(0.1)


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""
    total = len(lst)
    for i, elem in enumerate(lst, start=1):
        percent = i / total
        print_loading_bar(percent, total)
        yield i
