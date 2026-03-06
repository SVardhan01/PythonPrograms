n = 30

for i in [2,3,5]:
    while n%i==0:
        n //=i
if n==1:
    print("Ugly Number")
else:
    print("Not an Ugly Number")
        
        
