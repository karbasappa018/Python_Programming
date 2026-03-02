print("Enter the first number:")
No1 = input()

print("Enter the second number:")
No2 = input()

print(type(No1))
print(type(No2))

Ans = int(No1) + int(No2)  # str to integer like typecasting
print("Addition is:",Ans)

# Only foe the performing addition string is converted to
# integer after addition its again String is there.
print(type(No1))
print(type(No2))

