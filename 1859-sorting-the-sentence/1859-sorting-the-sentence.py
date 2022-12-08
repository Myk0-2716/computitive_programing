class Solution:
    def sortSentence(self, s: str) -> str:
        y = list(s.split())
        for i in range(len(y)):
            for j in range(0,len(y)-1):
                if y[j][-1] > y[j +1][-1]:
                    y[j],y[j+1] = y[j+1],y[j]
        li = []
        for it in y:
            li.append(it.replace(it[-1],''))
        z = ' '.join(li)
        return z
                    