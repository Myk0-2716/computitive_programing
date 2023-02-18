class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        nums.sort()
        for count,ele in list(enumerate(nums,start = 0)):
            if ele == target:
                l.append(count)
        return l
        