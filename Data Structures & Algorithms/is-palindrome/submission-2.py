class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute force: Time/Space O(1)
        import re
        s_ = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        midpoint = len(s_) // 2
        if len(s_) % 2 == 0:
            _ = s_[:midpoint]
            _.reverse()
            return _ == s_[midpoint:]
        else:
            _ = s_[:midpoint]
            _.reverse()
            return _ == s_[midpoint+1:]

        # Brute force:
        new_str = ""

        for i in s:
            if i.isalnum():
                new_str += i

        return new_str == new_str[::-1]