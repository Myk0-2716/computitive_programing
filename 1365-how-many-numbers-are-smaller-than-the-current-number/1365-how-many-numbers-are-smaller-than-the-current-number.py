class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        l = []
        for i in range(len(nums)):
            v = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    v += 1
            l.append(v)
        return l
                    
        