int maxv[100010];
int val[100010];

class Solution {
public:
    int maxProfit(vector<int> &prices) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function
		int ans = 0;
		int n = prices.size();
		if (n == 0)return 0;
		int m = prices[0];
		memset(maxv , 0 , sizeof(maxv));
		memset(val , 0 , sizeof(val));
		maxv[ n - 1] = prices[n - 1];
		
		val[0] = 0;
		for (int i = 1 ; i < n ; i ++){
			int tmp = prices[i] - m;
			m = min(m , prices[i]);
			val[i] = max(val[i - 1] , tmp);
			ans = max(ans , val[i]);
		}

		for (int i = n - 2 ; i >= 0 ; i --){
			maxv[i] = max(maxv[i + 1] , prices[i]);
		}

		for (int i = 1 ; i < n ; i ++){
			
			int a = maxv[i] - prices[i];
			int b = val[i - 1];
			ans = max(ans , a + b);

		}
		return ans;
	}
};

