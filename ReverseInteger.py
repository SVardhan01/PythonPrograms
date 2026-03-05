x = -123
rev = 0

sign = -1 if x<0 else 1

x = abs(x)
temp = x
while temp!=0:
    digit = temp%10
    rev = rev*10 + digit
    temp//=10
    
print(sign*rev)
