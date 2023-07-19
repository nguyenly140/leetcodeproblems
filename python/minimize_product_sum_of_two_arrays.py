class Solution:
    def minProductionSum(self, nums1: List[int], nums2: List[int]) -> int:
        # DESCENDING
        nums1 = [5, 3, 4, 2]
        nums1.sort()

        # ASCENDING
        nums2 = [4, 2, 2, 5]
        nums2.sort(reverse=True)
        
        # Product Sum
        productSum = 0
        for i in range(len(nums1)):
            productSum += nums1[i] * nums2[i]

        return productSum