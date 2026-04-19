import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(text)

        l = 0
        r = n - 1

        while l <= r:
            if text[l] != text[r]:
                return False
            l += 1
            r -= 1

        return True