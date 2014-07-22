/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int dp[100010][2];
bool v[100010][2];
int val[100010];
int ptr[100010][2];
int cnt;
int ans;

int tag(TreeNode *node){
    
    int x = cnt ++;
    val[x] = node->val;
    if (node->left)
        ptr[x][0] = tag(node->left);
    if (node->right)
        ptr[x][1] = tag(node->right);
    return x;

}

int f(int idx , int d){
    if (v[idx][d])return dp[idx][d];
    int l = ptr[idx][0];
    int r = ptr[idx][1];
    int ret = 0;
    if (d == 0){
        if (l != -1){
            int ll = f(l , 0);
            int lr = f(l , 1);
            ans = max(ans , ll + lr - val[l]);
            ret = max( 0 , max(ll , lr));
        }
    }
    else{
        if (r != -1){
            int rl = f(r , 0);
            int rr = f(r , 1);
            ans = max(ans , rl + rr - val[r]);
            ret = max( 0 , max(rl , rr));
        }
    }
    v[idx][d] = 1;
    return dp[idx][d] = ret + val[idx];
}

class Solution {
public:
    int maxPathSum(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        memset(dp , -1 , sizeof(dp));
        memset(ptr , -1 , sizeof(ptr));
        memset(v , 0 , sizeof(v));
        ans = -INT_MAX;
        cnt = 1;
        tag(root);
        int l = f(1 , 0);
        int r = f(1 , 1);
        ans = max(ans , l + r - val[1]);
        return ans;
    }
};

