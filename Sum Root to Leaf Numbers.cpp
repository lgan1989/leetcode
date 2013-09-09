/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int sum;

class Solution {
public:
    
    void sumCounts(TreeNode *node , int val){
       
       if (node == NULL)return;
       if (node->left == NULL && node->right == NULL){
           sum += val * 10 + node->val;
       }
       if (node->left != NULL){
           sumCounts(node->left , val * 10 + node->val);
       }
       if (node->right != NULL){
           sumCounts(node->right , val * 10 + node->val);
       }
        
    }

    int sumNumbers(TreeNode *root) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        sum = 0;
        sumCounts(root , 0);
        return sum;
    }
};

