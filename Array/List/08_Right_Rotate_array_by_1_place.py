# Right Rotate an array by one place

nums = [5,8,2,3,6,1]

n = len(nums)

# nums = [nums[-1]] + nums[0:n-1] 
# print(nums)  

# step 2 

temp = nums[-1]

for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)

