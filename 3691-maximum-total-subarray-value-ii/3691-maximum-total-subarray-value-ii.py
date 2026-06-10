import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        LOG = n.bit_length()

        mx = [[0] * n for _ in range(LOG)]
        mn = [[0] * n for _ in range(LOG)]

        for i in range(n):
            mx[0][i] = nums[i]
            mn[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            length = 1 << j

            for i in range(n - length + 1):
                mx[j][i] = max(mx[j - 1][i], mx[j - 1][i + half])
                mn[j][i] = min(mn[j - 1][i], mn[j - 1][i + half])

            j += 1

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        def get_value(l, r):
            length = r - l + 1
            p = lg[length]

            maximum = max(
                mx[p][l],
                mx[p][r - (1 << p) + 1]
            )

            minimum = min(
                mn[p][l],
                mn[p][r - (1 << p) + 1]
            )

            return maximum - minimum

        heap = []

        for l in range(n):
            r = n - 1
            heapq.heappush(heap, (-get_value(l, r), l, r))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans += -val

            if r > l:
                nr = r - 1
                heapq.heappush(
                    heap,
                    (-get_value(l, nr), l, nr)
                )

        return ans