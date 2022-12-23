class Solution:
    def romanToInt(self, s: str) -> int:
        
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}


        ans=0
        for a in range(len(s)-1):
            if rti[s[a]] < rti[s[a+1]]:
                ans = ans - rti[s[a]]
            else:   
                ans = ans + rti[s[a]]

        # So we add the last value and return the final ans
        return ans+rti[s[-1]]