class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        raw1 = set("qwertyuiop")
        raw2 = set("asdfghjkl")
        raw3 = set("zxcvbnm")
        
        k = []
        for word in words:
            l = []
            if set(word.lower()).intersection(raw1) == set(word.lower()):
                l.append('a')
            elif set(word.lower()).intersection(raw2) == set(word.lower()):
                l.append('a')
            elif set(word.lower()).intersection(raw3) == set(word.lower()):
                l.append('a')
            
            if len(l) > 0:
                k.append(word)
        return k