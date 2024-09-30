nums = [1,2,3,3,4]
c = False
for i in range(len(nums)) :
    for j in range(len(nums)) :
        if i != j and nums[i] == nums[j] :
            c = True
            break
print(c)
     
