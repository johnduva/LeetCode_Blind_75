class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Solve in a single pass by iterating and checking if the complement of current element exists in the hash map
        Time complexity: O(n)
        Space complexity: O(n)
        """
      
        seen = {}
        for i, num in enumerate(nums):
            comp = target-num
            if comp in seen:
                return [seen[comp], i]
            else:
                seen[num] = i
