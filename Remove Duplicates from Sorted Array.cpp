class Solution {
public:
    int removeDuplicates(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int ans = 0;
        if (n == 0)return 0;
        int p = 1;
        int v = A[0];
        ans = 1;
        while (p < n){

           while (p < n && A[p] == A[ans - 1]){
               p ++;
           }
           if (p >= n)break;
           swap(A[p] , A[ans]);
           ans ++;
           p ++;

        }


        return ans;
    }
};