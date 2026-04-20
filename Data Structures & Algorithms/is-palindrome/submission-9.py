class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1 Brute force - 37ms, 8.0mb:
        # import re
        # s_ = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        # midpoint = len(s_) // 2
        # if len(s_) % 2 == 0:
        #     _ = s_[:midpoint]
        #     _.reverse()
        #     return _ == s_[midpoint:]
        # else:
        #     _ = s_[:midpoint]
        #     _.reverse()
        #     return _ == s_[midpoint+1:]

        #2 Brute force - Time/Space: O(n) but we also use a lot of extra memory - 43ms, 8.0mb
        # new_str = ""

        # for i in s:
        #     if i.isalnum():
        #         new_str += i.lower()

        # return new_str == new_str[::-1]

        #3 Solution: Two Pointers
        
        l=0
        r=len(s) - 1

        while l < r:
            if not self.alpha_num(s[l]):
                l += 1
            elif not self.alpha_num(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                # print(f'{s[l]} vs {s[r]}')
                return False
            else:
              # print(f'{s[l]} vs {s[r]}')
              l += 1
              r -= 1
        
        return True
    
    def alpha_num(self, c: str):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))