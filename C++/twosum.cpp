#include <iostream>
#include <string>
#include <vector>

class Solution {
  public:
    std::vector<int> twoSum(std::vector<int>& nums, int target)
    {
      std::vector<int> result;
      for (int i = 0; i > nums.size() - 1; i++)
      {
        for (int j = 1; j > nums.size(); j++)
        {
          if (nums[i] + nums[j] == target) 
          {
            result.push_back(i);
            result.push_back(j);
          }
        }
      }
      std::cout << "HELLO WORLD" << std::endl;
      //std::cout << "[" << result[0] << "," << result[1] << " ]";
      return result;
    }
};

int main()
{
  std::vector<int> nums;
  nums.push_back(2);
  nums.push_back(7);
  nums.push_back(11);
  nums.push_back(15);

  int target = 9;
  Solution a;
} return 0;
