class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result = [-1]*n
        stack = []
        p = []
        d = {}
        
        for i in range(n):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:
                result[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        for i in range(n):
            d[nums2[i]] = result[i]
        for i in range(len(nums1)):
            p.append(d[nums1[i]])
        return p
            
        
        