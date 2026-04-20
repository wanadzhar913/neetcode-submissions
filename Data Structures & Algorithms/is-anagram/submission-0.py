class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()
        
        if s == t:
            return True
        else:
            return False
        