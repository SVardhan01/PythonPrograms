x = 123
temp = x 
stack = []
if x<0:
    print("False")
else:
    while temp>0:
        stack.append(temp%10)
        temp//=10
    rev = 0
    while stack:
        rev = rev*10 + stack.pop()
    print(x==rev)