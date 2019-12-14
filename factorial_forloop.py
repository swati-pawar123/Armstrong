n=int(input("Enter the Number:"))
result = 1
for i in range(n,0,-1):
    result = result * i
print("Factorial of",n,"is",result)