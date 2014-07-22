class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int pos[26];
        memset(pos , -1 , sizeof(pos));
        int len = s.length();
        int ans = 0;
        int offset = -1;
        if (len == 0)return ans;
        for (int i = 0 ; i < len ; i ++){
            if (pos[ s[i] - 'a' ]  < offset){
                int d = i - offset;
                ans = max(d , ans);
            }
            else{
                int d = i - pos[s[i]-'a'];
                ans = max(d , ans);
                offset = pos[s[i]-'a'];
            }
            pos[ s[i] - 'a' ] = i;
        }
        return ans;
    }
};