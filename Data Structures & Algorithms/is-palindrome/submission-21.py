class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join([char for char in s if char.isalnum()]).lower()
        #special_chars = "!?@#$%^&*"
        #s= s.strip(special_chars).lower()
        s = s.replace(" ", "")
        print (s[0:])
        print(s[::-1])
        return s[0:] == s[::-1]

