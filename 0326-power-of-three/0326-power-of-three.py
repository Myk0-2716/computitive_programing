class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n < 0:
            return False
        
        else:
            return 1162261467 % n == 0