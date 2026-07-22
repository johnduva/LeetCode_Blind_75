class Solution:
    def isValidParen(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{',  ']':'[',  ')':'('}
        
        for char in s:
            # If opening bracket, add to stack
            if char in mapping.values():
                stack.append(char)
            # If closing bracket (and top of stack isn't matching open bracket), return False
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        # Check if anything left in the stack
        return not stack
