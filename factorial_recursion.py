def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
n = int ( input("Enter the Number:"))
result=fact(n)
print("Factorial of",n,"is",result)