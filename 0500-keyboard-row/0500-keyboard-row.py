class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        raw1 = {'o', 'r', 'q', 't', 'i', 'u', 'y', 'e', 'w', 'p'}
        raw2 = {'g', 's', 'd', 'h', 'k', 'j', 'f', 'l', 'a'}
        raw3 = {'v', 'x', 'b', 'n', 'm', 'c', 'z'}
        
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