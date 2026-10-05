class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                x = stack.pop()

                if x == 0:
                    score = 1
                else:
                    score = 2 * x

                stack[-1] += score

        return stack[0]