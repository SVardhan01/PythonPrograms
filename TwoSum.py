nums = [3,2,4,5,1,7]

target = 4

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if i != j and nums[i] + nums[j] == target:
            print([i,j])