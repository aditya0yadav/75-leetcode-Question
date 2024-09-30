nums = [1,2,3,4]
seen  = set()
for i in nums :
    seen.add(i)
print(len(seen) != len(nums))