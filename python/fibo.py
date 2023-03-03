import math

class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        return int((pow(1 + sqrt5, n) - pow(1 - sqrt5, n)) / (pow(2, n) * sqrt5))

a = Solution()

print("F(0) = ",a.fib(0), "\nF(1) = ", a.fib(1), "\nF(2) = ", a.fib(2), "\nF(3) = ", a.fib(3), "\nF(4) = ", a.fib(4))
