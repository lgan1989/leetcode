class Solution {
public:
    string longestPalindrome(string s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int ans = 0 , len = 0;
        string res;
        int sLen = s.length();
        if (sLen == 0)return NULL;


        for (int i = 0 ; i < sLen ; i ++){
            len = 1;
            while (i + len < sLen && i - len >= 0 && s[i + len] == s[i - len]){
                len ++;
            }
            len --;
            int st = i - len;
            len = 1 + len * 2;
            if (len > ans){
                ans = len;
                res = s.substr(st , len);
            }


            len = 0;
            while (i - len >= 0 && i + 1 + len < sLen && s[i - len] == s[i + 1 + len]){
                len ++;
            }
            len --;
            st = i - len;
            len = 2 + len * 2;
            if (len > ans){
                ans = len;
                res = s.substr(st , len);
            }
        }


        return res;
    }
};