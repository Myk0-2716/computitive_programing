class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        nums.sort()
        nums.reverse()
        return str(nums[k - 1])