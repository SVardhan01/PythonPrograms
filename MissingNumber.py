nums = [1,3,0]

sums = 0
for num in nums:
    sums = sums+num
n = len(nums)
total = n*(n+1) // 2
required = total - sums
print(abs(required))

