class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if ord(s[l]) not in set([i for i in range(ord('A'), ord('Z') + 1)] + 
            [i for i in range(ord('a'), ord('z') + 1)] + 
            [i for i in range(ord('0'), ord('9') + 1)]):
                l += 1
            elif ord(s[r]) not in set([i for i in range(ord('A'), ord('Z') + 1)] + 
            [i for i in range(ord('a'), ord('z') + 1)] + 
            [i for i in range(ord('0'), ord('9') + 1)]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True