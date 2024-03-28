class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = []
        for num in nums:
            if num not in new_nums:
                new_nums.append(num)

        nums[:] = new_nums[:]

        return len(nums)
