class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []

        for i in range(n+1):
            nums.append(len(bin(i)[2:].replace('0', '')))
        
        return nums
        