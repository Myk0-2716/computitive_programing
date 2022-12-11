class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        
        for i in range(len(nums2)):
            d[nums2[i]] = -1
            
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                item = stack.pop()
                d[item] = nums2[i]
                
            stack.append(nums2[i])
            
        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]
        
        return nums1
        