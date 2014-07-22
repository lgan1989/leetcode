/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int ans = INT_MAX;
class Solution {
public:

    void dfs(TreeNode *node , int depth){
        if (!node->left && !node->right){
            ans = min(ans , depth);
            return;
        }
        if (node->left){
            dfs(node->left , depth + 1);
        }
        if (node->right){
            dfs(node->right , depth + 1);
        }
    }
    int minDepth(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ans = INT_MAX;
        if (root == NULL)
            return 0;

        dfs(root , 1);

        return ans;
    }
};