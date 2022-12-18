class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        k = list(s)
        
        for i in range(len(k)) :
            k = k[1:] + k[:1]
            if ''.join(k) == goal:
                return True
        return False
            
            
        