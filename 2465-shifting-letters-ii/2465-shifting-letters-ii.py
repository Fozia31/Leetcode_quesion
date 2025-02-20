class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        len_ = len(s) + 1

        shift = [0] * len_
        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                shift[end + 1] -= 1
            else:
                shift[start] -= 1
                shift[end + 1] += 1
        cur_sum = 0
        result = []
        for i in range(len(s)):
            cur_sum += shift[i]
            new_char = chr(((ord(s[i]) - ord('a') + cur_sum) % 26) + ord('a'))
            result.append(new_char)
        return "".join(result)


                # def forward(s_):
        #     for i in range(shift[0] , shift[1] + 1):
        #         if s_[i] == "z":
        #             s_[i] = "a"
        #         else:
        #             s_[i] = chr(ord(s_[i]) + 1)

        # def backward(s):
        #     for i in range(shift[0] , shift[1] + 1):
        #         if s_[i] == "a":
        #             s_[i] = "z"
        #         else:
        #             s_[i] = chr(ord(s_[i]) - 1)
        # s_=[]
        # for i in s:
        #     s_.append(i)
        
        # for shift in shifts:
        #     if shift[2] == 0:
        #         backward(s_)
        #     elif shift[2] == 1:
        #         forward(s_)
        # return "".join(s_)
        

