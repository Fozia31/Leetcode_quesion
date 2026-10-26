class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.segment_tree = [0] * (4 * self.n + 1)
        if self.n > 0:
            self.builder(0, 0, self.n - 1)

    def builder(self, idx, low, high):
        if low == high:
            self.segment_tree[idx] = self.nums[low]
            return self.segment_tree[idx]

        mid = (low + high) // 2
        left_side = self.builder(2 * idx + 1, low, mid)
        right_side = self.builder(2 * idx + 2, mid + 1, high)

        self.segment_tree[idx] = left_side + right_side
        return self.segment_tree[idx]

    def update(self, index: int, val: int) -> None:
        def update_val(idx, low, high):
            if low == high:
                self.segment_tree[idx] = val
                self.nums[index] = val
                return

            mid = (low + high) // 2
            if index <= mid:
                update_val(2 * idx + 1, low, mid)
            else:
                update_val(2 * idx + 2, mid + 1, high)
            self.segment_tree[idx] = (
                self.segment_tree[2 * idx + 1] + self.segment_tree[2 * idx + 2]
            )

        update_val(0, 0, self.n - 1)

    def sum_helper(self, idx, low, high, left, right):
        if low > right or high < left:
            return 0
        if left <= low and high <= right:
            return self.segment_tree[idx]

        mid = (low + high) // 2
        left_sum = self.sum_helper(2 * idx + 1, low, mid, left, right)
        right_sum = self.sum_helper(2 * idx + 2, mid + 1, high, left, right)
        return left_sum + right_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_helper(0, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)