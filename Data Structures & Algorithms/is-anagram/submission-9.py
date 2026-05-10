class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted (t.lower()) == sorted (s.lower())