class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1) Check length of nums vs unique values in nums 
        return len(set(nums)) != len(nums)
        
        # 2) Add values to 'seen' set as you loop through
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # 3) Using a dict instead of a set
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = num
        return False
