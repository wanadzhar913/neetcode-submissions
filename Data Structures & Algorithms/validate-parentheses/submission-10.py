class Solution:
    def isValid(self, s: str) -> bool:
        # Solution #1
        # if len(s) < 2:
        #     return False

        # hashset = {
        #     '{': '}',
        #     '[': ']',
        #     '(': ')'
        # }

        # if s[0] in hashset.values():
        #     return False

        # seen = []

        # for i in range(len(s)):
        #     if s[i] in hashset.keys():
        #         seen.append(s[i])
        #     else:
        #         if len(seen) == 0:
        #             seen.append(s[i])
        #         else:
        #             if s[i] == hashset[seen[-1]]:
        #                 seen.pop()
        #             else:
        #                 seen.insert(0, s[i])
        
        # if len(seen) == 0:
        #     return True
        # else:
        #     return False

        # Solution #2
        stack = []
        close_to_open = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False



        