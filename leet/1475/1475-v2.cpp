#include <iostream>
#include <stack>
#include <vector>

using namespace std;


class Solution {
public:

    vector<int> finalPrices(vector<int>& prices)
    {
        int size = prices.size();
        vector<int> ans(size);
        stack<int> st;

        int index = 0;
        st.push(index); // Push the first element in array onto stack
        index++;

        while (index < size)
        {
            // assert (!st.empty());
            if ( prices[index] > prices[st.top()] )
                st.push(index);
            else if ( prices[index] == prices[st.top()] )
            {
                while ( !st.empty() && prices[index] == prices[st.top()] )
                {
                    int top_index = st.top();
                    st.pop();

                    ans[top_index] = 0;
                }
                st.push(index);
            }
            else
            {
                // This stack will contain indices of all the elements that are not less than the current element
                stack<int> newStack;

                //if ( prices[index] < prices[st.top()])
                while ( !st.empty() && prices[index] <= prices[st.top()] )
                {
                    int top_index = st.top();
                    st.pop();

                    if ( prices[index] <= prices[top_index] )
                        ans[top_index] = prices[top_index] - prices[index];
                    else
                        newStack.push(top_index);
                }

                // Push all the elements in new stack to original stack
                while (!newStack.empty())
                {
                    int newIndex = newStack.top();
                    newStack.pop();
                    st.push(newIndex);
                }
                st.push(index);
            }
            index++;
        }

        while (!st.empty())
        {
            int top_index = st.top();
            st.pop();

            ans[top_index] = prices[top_index];
        }
        return ans;
    }
};


int main() {
    Solution s;
    vector<int> nums = {4, 8, 4};
    vector<int> result = s.finalPrices(nums);

    cout << "Result: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
