import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print "I have a secret"
print secret
print "It's a number from 1 to 99. I'll give you 6 tries."
while guess != secret and tries < 6:
	guess = input("What's yer guess?")
	if guess < secret:
		print "too low"
	elif guess > secret:
		print "too high"

	tries = tries + 1

if guess == secret:
	print "Avast"

else:
	print "No more guesses!"
	print "the secret number was", secret

