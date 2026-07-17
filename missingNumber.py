class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the "expected sum" as if there's no missing num
        exp_sum = n * (n+1) // 2
        curr_sum = sum(nums)
        return exp_sum - curr_sum
