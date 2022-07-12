from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        
        for bracket in s[1:]:
            
            if (not stack
                or (bracket in ('(', '[', '{')) 
                and stack[-1] in ('(', '[', '{')):
                
                stack.append(bracket)
            elif ((bracket == ')' and stack[-1] == '(')
                    or (bracket == ']' and stack[-1] == '[')
                    or (bracket == '}' and stack[-1] == '{')):
                
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False