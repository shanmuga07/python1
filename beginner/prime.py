while True:
	print("Enter 'x' for exit.")
	b = input("Enter any number: ")
	if b == 'x':
		break
	try:
		number = int(b)
	except ValueError:
		print("Please, enter a number...")
	else:
		for i in range(2, number):
			if number%i == 0:
				print(number, "is not a prime number.\n")
				break
		else:
			print(number, "is a prime number.\n")
