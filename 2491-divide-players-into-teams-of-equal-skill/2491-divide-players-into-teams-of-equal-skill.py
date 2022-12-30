class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        start = 0
        end = len(skill)-1
        li = []
        skill.sort()
        while start < end:
            li.append([skill[start], skill[end]])
            start +=1
            end -=1
        result = list(map(sum,li))
        chem = 0
        if len(set(result)) == 1:
            for it in li:
                chem += it[0]*it[1]
            return chem
        else:
            return -1
            
        