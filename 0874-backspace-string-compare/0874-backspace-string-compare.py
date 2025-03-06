class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for ss in s:
            if ss == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ss)


        for tt in t:
            if tt == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(tt)
        return "".join(stack_s) == "".join(stack_t)
        