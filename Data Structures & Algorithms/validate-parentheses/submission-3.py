class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = []

        chars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in chars:
                stack.append(c)
            else:
                if not stack or chars[stack.pop()] != c:
                    return False


        return not stack
        