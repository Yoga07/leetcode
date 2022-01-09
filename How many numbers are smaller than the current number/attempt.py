class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def merge_sort(array: List[int]) -> List[int]:
            if len(array) > 1:
                mid = len(array) // 2
                    
                L = array[:mid]
                R = array[mid:]

                i = j = k = 0

                merge_sort(L)
                merge_sort(R)

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        array[k] = L[i]
                        i += 1
                    else:
                        array[k] = R[j]
                        j += 1
                    k += 1
                    
                # check for leftover in L and R
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1
                    
                while j < len(R):
                    array[k] = R[j]
                    j += 1
                    k += 1
            
        original_nums = nums.copy()
        
        merge_sort(nums)

        return [nums.index(num) for num in original_nums] 