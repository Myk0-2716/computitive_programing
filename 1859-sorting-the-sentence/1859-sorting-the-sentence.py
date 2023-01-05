class Solution:
    def sortSentence(self, s: str) -> str:
        l = list(s.split())
        n = len(l)
        for i in range(n):
            for j in range(n-1):
                if l[j][-1] > l[j+1][-1]:
                    l[j],l[j+1] = l[j+1],l[j]
        li = []
        for it in l:
            li.append(it.replace(it[-1], ''))
        z = ' '.join(li)
        return z