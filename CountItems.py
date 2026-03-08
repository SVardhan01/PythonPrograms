items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]

rulekey = 'Type'
rulevalue = 'phone'

if rulekey == 'Type':
    index = 0
elif rulekey == 'Color':
    index = 1
else:
    index = 2

count = 0
for item in items:
    if item[index] == rulevalue:
        count+=1

print(count)
