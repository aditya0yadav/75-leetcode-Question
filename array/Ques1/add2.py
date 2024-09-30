nums = [1,2,3,4,5]
target = 7
hump = {}

for i in range(len(nums)) :
    if target - nums[i] in hump :
        print(hump[target - nums[i]],i)
    hump[nums[i]] = i