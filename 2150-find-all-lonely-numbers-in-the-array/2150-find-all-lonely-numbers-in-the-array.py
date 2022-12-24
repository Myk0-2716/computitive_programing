from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        v = []
        for it in d:
            if d[it] == 1:
                if d[it+1] == 0 and d[it-1] == 0:
                    v.append(it)
        
        
        return v