class Solution {
public:
    int removeDuplicates(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (n == 0)return 0;
        int p = 1;
        int ans = 1;
        int c = 1;
        while (p < n){
            
            if (c == 1){
                if (A[p] == A[ans - 1])
                    c ++;
                swap(A[p] , A[ans]);
                p ++;
                ans ++;
            }
            else{
                while (p < n && A[p] == A[ans - 1]){
                    p ++;
                }
                if (p >= n)break;
                swap(A[p] , A[ans]);
                p ++;
                ans ++;
                c = 1;
            }
            
        }
        return ans;
    }
};