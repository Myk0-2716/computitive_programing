class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums)-1
        c = 0
        nums.sort()
        while start < end:
            if nums[start] + nums[end] > k:
                end -=1
            elif nums[start] + nums[end] < k:
                start +=1
            else:
                start +=1
                end -=1
                c +=1
            
        return c
                