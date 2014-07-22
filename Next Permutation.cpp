class Solution {
public:
    void nextPermutation(vector<int> &num) {
        int len = num.size();
        int pos = -1;
        for (int i = len - 1 ; i >= 0 ; i --){
            int p = -1;
            int m = -1;
            for (int j = i + 1 ; j < len ; j ++){
                if (num[j] > num[i]){
                    if (m == -1 || num[j] < m){
                        m = num[j];
                        p = j;
                    }
                }
            }
            if (p != -1){
                swap(num[i] , num[p]);
                pos = i;
                break;
            }
        }
        
        
        sort(num.begin() + pos + 1 , num.end());
        
    }
};

