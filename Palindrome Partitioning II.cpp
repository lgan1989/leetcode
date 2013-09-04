int dp[2010];
bool check[2010][2010];
class Solution {
public:

	void init(string s){

		memset(dp , 0 , sizeof(dp));
		memset(check , 0 , sizeof(check));
		int len = s.length();
		for (int i = 0 ; i < len ; i ++){

			check[i][i] = 1;
			//odd
			for (int k = 1 ; i + k < len && i - k >= 0 ; k ++){

				if ( s[i + k] != s[i - k])break;
				check[i - k][i + k] = 1;

			}
			//even
			for (int k = 0 ; i + 1  + k < len && i - k >= 0 ; k ++){

				if ( s[i - k] != s[i + 1 + k] )break;
				check[i - k][i + 1 + k] = 1;

			}

		}

	}

	int minCut(string s) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function
		init(s);
		int len = s.length();

		dp[0] = 0;
		int ret = 9999999;
		for (int i = 1 ; i < len ; i ++){

			int temp = 999999;
			if (check[0][i] == 1){
				dp[i] = 0;
				continue;
			}
			for (int j = 0 ; j < i ; j ++){

				if ( check[i - j][i] == 1){

					temp = min(temp , dp[i - j - 1] + 1);

				}

			}
			dp[i] = temp;

		}

		return dp[len - 1];

	}
};

