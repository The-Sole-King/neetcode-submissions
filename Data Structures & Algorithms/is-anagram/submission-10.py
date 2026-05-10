class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(sorted (t.lower()))
        return sorted (t.lower()) == sorted (s.lower())