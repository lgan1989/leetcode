map < int , vector< vector < string > >> dp;
bool check[2010][2010];
string str;

class Solution {
public:

    void init(string s){

		memset(check , 0 , sizeof(check));
		int len = s.length();
		dp.clear();
		str = s;
		for (int i = 0 ; i < len ; i ++){

			for (int j = 0 ; i - j >= 0 && i + j < len ;  j++){
				//odd
				if (s[i - j] != s[i + j])break;
				check[i - j][i + j] = 1;
			}
			for (int j = 0 ; i - j >= 0 && i + 1 + j < len ; j ++){
				//even
				if (s[i - j] != s[i + 1 + j])break;
				check[i - j][i + 1 + j] = 1;
			}
		}
	}

	vector < vector<string> > dfs(int idx){

		if (dp.count(idx))return dp[idx];
		vector< vector<string> > ret;
		ret.clear();
		if ( check[0][idx] ){
			vector < string > tmp;
			tmp.clear();
			tmp.push_back( str.substr(0 , idx + 1) );
			ret.push_back(tmp);
		}
		for (int i = 0 ; i < idx ; i ++){
			if ( check[i + 1][idx] ){
				vector < string> tmp;
				tmp.clear();
				vector < vector < string > > r = dfs(i);
				for (int j = 0 ; j < r.size() ; j ++){
					r[j].push_back( str.substr(i + 1 , idx - i) );
					ret.push_back( r[j] );
				}
			}
		}
		return dp[idx] = ret;
	}

	vector<vector<string>> partition(string s) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function
		init(s);
		int len = s.length();

		return dfs(len - 1);
	}
};

