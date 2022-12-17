class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        v = []
        for index,ele in enumerate(nums,0):
            if ele == target:
                v.append(index)
        return v