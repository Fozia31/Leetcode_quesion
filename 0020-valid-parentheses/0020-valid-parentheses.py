class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = [")" , "]" , "}"]
        stack = []
        for i in s:
            if i in open_brackets:
                if stack:
                    if stack[-1] == "("  and i == open_brackets[0] :
                        stack.pop()
                    elif stack[-1] == "["  and i == open_brackets[1] :
                        stack.pop()
                    elif stack[-1] == "{"  and i == open_brackets[2] :
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(i)
                
        if stack:
            return False
        else:
            return True

                

        