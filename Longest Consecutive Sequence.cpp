map <int , int> h;

int ans;
class Solution {
public:

    int longestConsecutive(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        h.clear();

        int ret = 0;
        int len = num.size();
        for (int i = 0 ; i < len ; i ++)h[num[i]] = 1;
        for (int i = 0 ; i < len ; i ++){
            int tmp = 1;
            if (h[num[i]] == 0)continue;
            h[num[i]] = 0;
            int l = num[i] - 1;
            while ( h[l] != 0 ){
                tmp ++;
                h[l] = 0;
                l --;
            }
            int r = num[i] + 1;
            while ( h[r] != 0 ){
                tmp ++;
                h[r] = 0;
                r ++;
            }
            ret = max(tmp , ret);
        }
        return ret;
        
    }
};

