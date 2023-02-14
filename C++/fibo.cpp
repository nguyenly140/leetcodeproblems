#include <iostream>
#include <math.h>

class Solution {
  public:
    int fib(int n) {
      return (pow(1 + sqrt(5), n) - pow(1 - sqrt(5), n)) / (pow(2, n) * sqrt(5));
    }
}; 

int main()
{
  Solution x;
  std::cout << "F(0) = " << x.fib(0) << std::endl;
  std::cout << "F(1) = " << x.fib(1) << std::endl;
  std::cout << "F(2) = " << x.fib(2) << std::endl;
  std::cout << "F(3) = " << x.fib(3) << std::endl;
  std::cout << "F(4) = " << x.fib(4) << std::endl;
  return 0;
}
