/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector <int> ans;
    void dfs(TreeNode* node){
        if (node == NULL)
            return;
        ans.push_back(node->val);
        dfs(node->left);
        dfs(node->right);
    }
    vector<int> preorderTraversal(TreeNode *root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ans.clear();
        dfs(root);
        return ans;
    }
};