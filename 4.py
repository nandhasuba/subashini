while True:
	print("Enter '0' for exit.")
	char = input("Enter any character: ")
	if char == '0':
		break
	else:
		if((char>='a' and char<='z') or (char>='A' and char<='Z')):
			print(char, "is an alphabet.\n")
		else:
			print(char, "is not an alphabet.\n")
