import heapq

class Solution:
    def minProductionSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Easier to descend the numbers in one of the array and ascend the numbers in the other
        # DESCENDING
        # nums1 = [5, 3, 4, 2]
        # nums1.sort()

        # # ASCENDING
        # nums2 = [4, 2, 2, 5]
        # nums2.sort(reverse=True)
        
        # # Product Sum
        # productSum = 0
        # for i in range(len(nums1)):
        #     productSum += nums1[i] * nums2[i]

        # return productSum

        # Priority Queue
        nums1.sort()

        ans = 0

        # initialize max heap (needs to add existing list with "-x for x in 'list'")- empty priorityqueue
        pq = [-x for x in nums2]
        heapq.heapify(pq)

        for i in nums1:
            ans += i * -heapq.heapop(pq)

        return ans