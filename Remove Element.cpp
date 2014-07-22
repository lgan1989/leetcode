class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int c = 0;
        for (int i = 0 ; i < n ; i ++)
            c += elem == A[i];
        for (int i = 0 ; i < n ; i ++){
            if (A[i] == elem){
                for (int j = n - c ; j < n ; j ++){
                    if (A[j] != elem){
                        swap(A[j] , A[i]);
                    }
                }
            }
        }
        return n - c;
    }
};

