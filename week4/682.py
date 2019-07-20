class Solution:
    def calPoints(self, ops: List[str]) -> int:

        sum = 0
        stack = []

        for op in ops:
            if op == "C":
                sum -= stack.pop()
            else:
                if op.isnumeric() or "-" in op:
                    num = int(op)

                elif op == "+":
                    num = (stack[-1] if stack else 0) + (stack[-2] if stack else 0)

                else:
                    num = stack[-1] * 2
                sum += num
                stack.append(num)
        return sum
            