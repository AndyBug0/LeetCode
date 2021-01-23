class Solution(object):
    def test(self, nums, left, right):
        for i in range(left, right):
            print(nums[i], end=' ')
        print("")

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = 0
        sum_ = 0
        size = 0
        while sum_ < s:         # [ , )
            if right >= len(nums):
                return 0
            sum_ += nums[right]
            right += 1
            # self.test(nums, left, right)
        size = right - left

        while right < len(nums):
            while sum_ >= s:
                sum_ -= nums[left]
                left += 1
                size -= 1
                # self.test(nums, left, right)
            sum_ -= nums[left]
            left += 1
            sum_ += nums[right]
            right += 1
            # self.test(nums, left, right)
        while sum_ >= s:
            sum_ -= nums[left]
            left += 1
            size -= 1
            # self.test(nums, left, right)
        return size + 1