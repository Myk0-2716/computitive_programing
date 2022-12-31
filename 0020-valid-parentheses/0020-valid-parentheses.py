class Solution:
    def isValid(self, s: str) -> bool:
        left = "({["
        right = ")}]"
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not stack:
                    return False
                elif right.index(c) != left.index(stack.pop()):
                    return False
        return not stack

            