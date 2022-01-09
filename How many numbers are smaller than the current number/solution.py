class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mapping = {}
        
        for idx, num in enumerate(sorted(nums)):
            if num not in mapping:
                mapping[num] = idx
                
        return [mapping[num] for num in nums]