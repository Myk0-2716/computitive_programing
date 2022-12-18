class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        z = []
        y = []
        x = int(len(nums)/2)
        for i in range(len(nums)):
            if i <= x:
                z.append(nums[i])
            else:
                y.append(nums[i])
        i = 1
        for it in y:
            z.insert(i,it)
            i += 2
        return z
        