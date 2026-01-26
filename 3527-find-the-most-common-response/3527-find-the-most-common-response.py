class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        freq = {}

        for day in responses:
            for resp in set(day):
                freq[resp] = freq.get(resp, 0) + 1

        ans = ""
        max_count = 0

        for resp in freq:
            if freq[resp] > max_count or (freq[resp] == max_count and resp < ans):
                max_count = freq[resp]
                ans = resp

        return ans
