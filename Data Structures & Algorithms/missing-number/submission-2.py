class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Solution #1: Time - O(n^2), Space - O(1)
        # Reasoning: Your loop runs `n` times (the range is `len(nums) + 1`).
        # Inside that loop, the line `if i not in nums` performs a linear
        # search on the list. A search inside a loop means you are essentially
        # doing `n * n` work.
        # x = 0

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         x += i
        
        # return x

        # Solution #2: Time: O(n), Space: O(1)
        # NOTE: In Python 3, `range()` is a "lazy" iterable (a generator-like object).
        # It does not create a list of numbers in memory; it just calculates the next
        # number on the fly. So, while the code is perfectly valid, calling `sum(range(...))`
        # still technically performs a loop behind the scenes. If you want to be truly
        # elite, you can replace that second sum with the Gauss Summation Formula.
        # return abs(sum(nums) - sum(range(len(nums) + 1)))

        # Solution #3: # O(n) to sum the list, O(1) space
        n = len(nums)

        # We use the Gaussian Summation formula as it allows for
        # quick calculation of the sum of consecutive integers from 1 to `n`
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        
        # Intuition: If you calculate the expected sum and subtract the
        # actual sum of your list, the remainder is your missing number.
        return expected_sum - actual_sum

        # Solution 4: Time: O(n), Space: O(1)



        