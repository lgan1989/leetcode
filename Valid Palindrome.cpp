class Solution {
public:
	bool isPalindrome(string s) {
		// Start typing your C/C++ solution below
		// DO NOT write int main() function
		string ns = "";
		for (int i = 0 ; i < s.length() ; i ++){
			if (isalpha(s[i]) || isdigit(s[i]))ns += toupper(s[i]);
		}
		int len = ns.length();
		if (len == 0)return true;

		for (int i = 0 ; i < len/2 ; i ++){
			if ( ns[i] != ns[len - 1 - i] ){
				return false;
			}
		}
		return true;

	}
};