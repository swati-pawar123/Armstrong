secret_word = "xyz"
guess=" "
guess_limit=3
guess_count=0
out_of_guesses=False
while guess != secret_word and not(out_of_guesses):
	if guess_count < guess_limit:
		guess=input("Enter Guess:")
		guess_count+=1
	else: out_of_guesses=True
if out_of_guesses:
	print("You Lose")
else:
	print("You Win")
