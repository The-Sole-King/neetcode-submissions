class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted (s.lower())
        sorted_t =sorted (t.lower())


        return sorted (t.lower()) == sorted (s.lower())