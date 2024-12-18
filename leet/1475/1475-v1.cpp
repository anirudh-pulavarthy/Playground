#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int discount(int index, vector<int>& prices)
    {
        int len = prices.size();
        int cur = index + 1;
        while ( cur < len )
        {
            if (prices[cur] <= prices[index])
                return prices[cur];
            cur++;
        }
        return 0;
    }

    vector<int> finalPrices(vector<int>& prices) {

        vector<int> ans(prices.size());
        int i = 0;
        for (auto price : prices)
            ans[i++] = price - discount(i, prices);

        return ans;
    }
};