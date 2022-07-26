def twoSum(nums, target):
    res = dict()
    
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        
        if num in res:
            return [res[num], i]
        else:
            res[complement] = i
            

print(twoSum([1, 2, 3], 4))
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
