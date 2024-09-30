nums = [1,2,3,4,5]
target = 9
cut = False
a,b = 0,0
for i in nums :
    for j in nums :
        if i + j == target:
            cut = True
        a,b = i,j
    if cut :
        break
print(a,b)