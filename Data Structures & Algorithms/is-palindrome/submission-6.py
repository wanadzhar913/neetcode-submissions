class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1 Brute force - 37ms, 8.0mb:
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

        #2 Brute force - Time/Space: O(n) but we also use a lot of extra memory - 43ms, 8.0mb
        # new_str = ""

        # for i in s:
        #     if i.isalnum():
        #         new_str += i.lower()

        # return new_str == new_str[::-1]

        # #3 Solution