nums = [1,2,3,1,3]

freq = {}
found = False

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for value in freq:
    if freq[value] >= 2:
        print("True")
        found = True
        break

if not found:
    print("False")