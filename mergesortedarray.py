class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        total = m+n
        new_nums1 = nums1[0:m] + nums2 [0:n]
        nums1[0:total] = new_nums1[0:total]
        nums1.sort()
        
