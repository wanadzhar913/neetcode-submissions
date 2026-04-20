class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s_ = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s_)
        midpoint = len(s_) // 2
        import re
        s_ = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        midpoint = len(s_) // 2
        if len(s_) % 2 == 0:
            print(f'even: {s_[:midpoint].reverse()} vs {s_[midpoint:]}')
            _ = s_[:midpoint]
            _.reverse()
            return _ == s_[midpoint:]

        else:
            print(f'odd: {s_[:midpoint].reverse()} vs {s_[midpoint+1:]}')
            _ = s_[:midpoint]
            _.reverse()
            return _ == s_[midpoint+1:]