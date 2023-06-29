# strong-arm array approach
class SparseVector:
    def __init__(self, nums: List[int]):
        self.num = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # used zip() function it takes 2 objects/list and pairs them which each respective index
        # ex. list1 = [1, 2, 3, 4] and list2 == [5, 4, 3, 2, 1], zip(list1, list2) = [(1, 5), (2, 4), (3, 3)]
        # for nums1, nums2 in zip(self.num, vec.num):
        #     result += nums1 * nums2
        # return result
        return sum([self.num[i] * vec.num[i] for i in range(len(vec.num))])

# hash set
class SparseVector:
    def __init__ (self, nums: List[int]):
        self.nonzeros = {}
        # used an enumerate() function adds a counter as the key to whatever is being enumerated
        # ex. list1 =  [1, 3, 5, 7], enumerate(list1) = [(0,1), (1,3), (2, 5), (3, 7)]
        # grabbing all the values in "nums" list and enumerating it, then storing all the non zero values 
        for i, n in enumerate(nums):
            if n != 0:
                self.nonezeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # for loop grabs both the index "i" and the values "n" from the array nonzeros and used .item() to grab all 
        for i, n in self.nonzeros.item():
            # then compare the index "i", if equal to any enumerate values in vector "nonzeros", if they do equal, multiple
            # both the value in self.nonzeros and the value in vec.nonzeros together
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
    
# index-value pairs
class SparseVector:
    def __init__(self, nums: List[int]):
        self.num = []
        # used an enumerate() function adds a counter as the key to whatever is being enumerated
        # ex. list1 =  [1, 3, 5, 7], enumerate(list1) = [(0,1), (1,3), (2, 5), (3, 7)]
        # grabbing all the values in "nums" list and enumerating it, then storing all the non zero values 
        for i, n in enumerate(nums):
            if n != 0:
                self.num.append([i, n])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        x, y = 0, 0
        # used while loops to get the lengths of both vec and self then compare them with each other value in their index-value pair
        while x < len(self.num) and y < len(vec.num):
            # if index at x and y for self and vec where value location is at 0 is equal to each other then multple them together then increment both x and y
            if self.num[x][0] == vec.num[y][0]:
                result += self.num[x][1] * vec.num[y][1]
                x += 1
                y += 1
            # if num at index x is less than vec at index y then increment self because it is less untill either they are equal or greater
            elif self.num[x][0] < vec.num[y][0]:
                x += 1
            else:
                y += 1
        return result