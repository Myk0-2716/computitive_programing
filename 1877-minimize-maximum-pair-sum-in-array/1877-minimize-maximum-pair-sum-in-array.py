class Solution:
    def minPairSum(self, nums: List[int]) -> int: 
        nums.sort()
        start = 0
        end = len(nums)-1
        li = []
        while start < end:
            li.append([nums[start],nums[end]])
            start +=1
            end-=1
        p = []
        for it in li:
            p.append(it[0]+ it[1])
        return max(p)
        