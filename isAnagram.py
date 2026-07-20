class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The 'Counter' function creates a dict where values are char counts (in string)
        from collections import Counter
        # 'anagram' -> {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}
        return Counter(s) == Counter(t)
