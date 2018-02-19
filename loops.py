
states = ["NY", "TX", "HI", "CA", "NJ", "MA"]

for state in states:
	print(states)

countdown = 10

while countdown >= 0:
	countdown -= 1
	if (countdown == 0):
		print("HAPPY NEW YEAR!!!!!")
		break
	print(countdown)


names = ["Potter", "Bond", "Anderson"]

while names:
	print("Howdy Mr." + names.pop())
