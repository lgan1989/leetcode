class Solution:
    # @return a boolean
    
    def isValid(self, s):
        stack = []
        match = {')' : '(' , ']' : '[' , '}' : '{'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.insert(0 , c)
            else:
                if len(stack) > 0:
                    top = stack[0]
                    stack = stack[1:]
                    if top != match[c]:
                        return False
                else:
                    return False
        return len(stack) == 0