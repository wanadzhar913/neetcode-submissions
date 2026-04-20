class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        hashset = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        if s[0] in hashset.values():
            return False

        seen = []

        for i in range(len(s)):
            if s[i] in hashset.keys():
                seen.append(s[i])
            else:
                if len(seen) == 0:
                    seen.append(s[i])
                else:
                    if s[i] == hashset[seen[-1]]:
                        seen.pop()
                    else:
                        seen.insert(0, s[i])
        
        if len(seen) == 0:
            return True
        else:
            return False



        