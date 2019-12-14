def upper_lower(string):
    d = {"upper": 0, "lower": 0}
    for char in string:
        if char.isupper():
            d["upper"] += 1
        elif char.islower():
            d["lower"] += 1
        else:
            pass
    print("no.of uppercase letters in string", d["upper"])
    print("no.of lowercase letters in string", d["lower"])


print(upper_lower(input("Enter a string:")))

