class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c +=1
            l.append(c)
        return l
        