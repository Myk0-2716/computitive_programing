class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = []
        for count,ele in enumerate(nums,0):
            if ele == target:
                l.append(count)
        return l