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
    bool isSameTree(TreeNode *p, TreeNode *q) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (!p && !q){
            return true;
        }
        if (p && q){

            if (p->val != q->val)
                return false;
            bool b1 = 0 , b2 = 0;
            if (!p->left && !q->left){
                b1 = 1;
            }
            else if (p->left && q->left){
                b1 = isSameTree(p->left , q->left);
            }
            else b1 = 0;
            if (!p->right && !q->right){
                b2 = 1;
            }
            else if (p->right && q->right){
                b2 = isSameTree(p->right , q->right);
            }
            else b2 = 0;
            return b1 && b2;
        }
        else return false;
    }
};