from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for x in range(0, length):
        for y in range(x+1, length):
            if (nums[x] + nums[y]) == target:
                return [x,y]
    
    return [0]

print(twoSum(nums = [2, 7, 11, 15], target = 9))
print(twoSum(nums = [3, 2, 4], target = 6))
print(twoSum(nums = [3, 3], target = 6))