# strong-arm array approach
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for nums1, nums2 in zip(self.nums, vec.nums):
            result += nums1 * nums2
        return result

# hash set
class SparseVector:
    def __init__ (self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonezeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.nonzeros.item():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
    
# index-value pairs
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, n in enumerate(nums):
            if n != 0:
                self.nums.append([i, n])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        x, y = 0, 0

        while x < len(self.nums) and y < len(vec.nums):
            if self.nums[x][0] == vec.nums[y][0]:
                result += self.nums[x][1] * vec.nums[y][1]
                x += 1
                y += 1
            elif self.nums[x][0] < vec.nums[y][0]:
                x += 1
            else:
                y += 1
        return result