class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        def oprr(a, b, opr):
            if opr == "+":
                stack.append(b + a)
            elif opr == "-":
                stack.append(b - a)
            elif opr == "*":
                stack.append(b * a)
            else:
                stack.append(int(b / a)) 
        stack = []
        opr = ["+", "-", "*", "/"]
        for i in tokens:
            if i in opr:
                a = stack.pop()  
                b = stack.pop()  
                oprr(a, b, i)
            else:
                stack.append(int(i)) 
        
        return stack[-1]