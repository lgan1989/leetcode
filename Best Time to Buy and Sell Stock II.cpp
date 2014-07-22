class Solution {
public:
    int maxProfit(vector<int> &prices) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int ans = 0;
        int n = prices.size();
        for (int i = 1 ; i < n ; i ++){
            int t = prices[i] - prices[i - 1];
            if (t > 0)ans += t;
        }
        return ans;
    }
};

