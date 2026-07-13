class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Two pointers, one for each word (both moving left to right)
        Note: appending to a list is faster that +='ing to a string
        
        Time complexity: O(m + n)
        We iterate through all characters.

        Space complexity: O(m + n)
        We put all characters into the list.
        """

        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
