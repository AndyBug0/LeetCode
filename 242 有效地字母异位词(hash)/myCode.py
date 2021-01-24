class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = [0 for i in range(26)]
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if alphabet[i] > 0:
                return False
        return True