class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        x = sentence.split()
        for i in range(len(x)):
            if x[i][:len(searchWord)] == searchWord:
                return i+1
        return -1
        