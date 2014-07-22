class Solution {
public:

    bool canJump(int A[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int p = 0;
        bool flag = false;
        for (int i = 0 ; i < n ; i ++){
            if (p >= i)
                p = max(p , i + A[i]);
            else
                break;
            if (p >= n - 1)
                flag = true;
        }
        return flag;
    }
};