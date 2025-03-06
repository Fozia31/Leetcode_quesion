class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for part in paths:
            if part == "" or part == ".":  
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        ans = "/" + "/".join(stack)
     
        return ans
                


        