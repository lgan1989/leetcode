class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        for (int i = 0 ; i < n ; i ++){
            A[m ++] = B[i];
        }
        sort(A , A + m);
    }
};