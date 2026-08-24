def funcDoinStu (n, c):
	timesUDoStu = n * c + n - c
	stuff = 0
	for i in range(timesUDoStu):
		print(f"I be doin stuff! see? {n * c / (i + 1) + i - n}")
		stuff = stuff + (timesUDoStu % (c + i + n))
	print("stuff done.")
	return stuff

funcDoinStu(3,8)