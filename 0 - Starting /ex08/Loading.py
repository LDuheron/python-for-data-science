import time

def get_percent(total: int):
	for i in range(total):
		percent = (i + 1) / total
		yield percent


def	print_loading_bar(percent: int, total: int):
	bar_len = 30
	bar = int((percent * 30))
	blank = int((1 - percent) * bar_len)
	bar_str = bar * "=" + blank * " "
	print(f"{percent * 100}%| [ {bar}{blank}] | {percent * total}/{total}", end="\r", flush=True)
	time.sleep(1)

if __name__ == "__main__":
	total = 10
	for n in get_percent(total):
		print_loading_bar(n, total)


# def ft_tqdm(lst: range) -> None:
# 	total = len(lst)
# 	n = get_percent(total)
# 	print_loading_bar(n, total)
