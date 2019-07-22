class Solution:
    def scoreOfParentheses(self, S: str) -> int:
    
        stack = [0]
        for c in S:
            if c == "(":
                stack.append(0)
            else:      
                top = stack.pop()
                stack[-1] += max(1, 2*top)

        return stack.pop()