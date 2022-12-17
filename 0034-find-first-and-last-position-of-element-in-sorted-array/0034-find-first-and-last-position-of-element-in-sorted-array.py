class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        v = []
        z = []
        for index,ele in enumerate(nums,0):
            if ele == target:
                v.append(index)
        
        if not v:
            return [-1,-1]
        elif len(v) == 1:
            return 2*v
        elif len(v) > 0:
            z.append(v[0])
            z.append(v[-1])
            return z
            
        
        else:
            return v