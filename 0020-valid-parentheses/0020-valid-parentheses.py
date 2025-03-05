class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i in ["]","}",")"]:
                if stack:
                    if (stack[-1]=="[" and i=="]") or (stack[-1]=="{" and i=="}") or(stack[-1]=="(" and i==")"):
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack:
            return False
        return True
        