def vowel(word):
	vowels="AEIOUaeiou"
	for vowel in vowels:
		word=word.replace(vowel,"g")
	return word
print(vowel(input("Enter a string:")))

