num=int(input("Enter the Number:"))
s=0
temp=num
while temp > 0:
    c=temp%10
    s+=c**3
    temp//=10
if num==s:
    print(num," is Armstrong Number")
else:
    print(num,"Not Armstrong Number")