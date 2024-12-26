#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {

        std::vector<int> v1 = {1, 2, 3, 4}; // Example vector
        std::vector<int> v2;

        // Resize v2 to twice the size of v1
        v2.resize(2 * v1.size());
    
        // Copy v1 into the first half of v2
        std::copy(v1.begin(), v1.end(), v2.begin());
    
        // Copy v1 into the second half of v2
        std::copy(v1.begin(), v1.end(), v2.begin() + v1.size());
        
        
    }
};