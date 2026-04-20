class Solution:
    def reverseBits(self, n: int) -> int:
        # **Solution 1:** Brute Force - Time/Space: O(logn)
        # **Key Intuition:** You are reading bits from right → left,
        # then placing them left → right in a 32-bit number.
        # multiplicator = []
        
        # **Intuition:** read the binary digits from right to left.
        # while n:
            # **Intuition:** Is the least significant bit (LSB) a 1 (2^0)?
            # if n % 2 == 1:
            #     multiplicator.append(1)
            # else:
            #     multiplicator.append(0)
            # **Intuition:** Shift everything right → discard the bit we just read.
            # n = n >> 1
        
        # output = 0
        # for i, bit_num in zip(multiplicator, reversed(range(32))):
        #     if i != 0:
                # **Intuition:** Since binary numbers are just sums of powers of two, we're just turning on that bit in the final number.
                # output += 2**(bit_num)
        
        # return output

        # **Solution 2:** Time/Space: O(1)
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res




        