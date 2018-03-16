number = 10
guess = 1
print("guess a number!")
while guess != number:
	guess = int(input("guess a number:"))
	if guess == number:
		print("congratulation!")
	elif guess > number:
		print("number is big")
	elif guess < number:
		print("number is small")
