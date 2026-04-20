class Solution:
    # Solution: Cheating
    def countBits(self, n: int) -> List[int]:
        # nums = []

        # for i in range(n+1):
        #     nums.append(len(bin(i)[2:].replace('0', '')))
        
        # return nums
    
        nums = []

        for i in range(n+1):
            count = 0
            x = i

            while x:
                if x % 2:
                    count += 1
                x = x >> 1
            nums.append(count)
        
        return nums
        