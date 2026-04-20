class Solution:
    def reverseBits(self, n: int) -> int:
        multiplicator = []
        
        while n:
            if n % 2 == 1:
                multiplicator.append(1)
            else:
                multiplicator.append(0)
            n = n >> 1
        print(multiplicator)
        
        output = 0
        for i, bit_num in zip(multiplicator, reversed(range(32))):
            print(bit_num)
            print(i)
            print(output)
            if i != 0:
                output += 2**(bit_num)
        
        return output



        