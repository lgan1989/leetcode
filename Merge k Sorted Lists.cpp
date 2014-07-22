/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ListNode *node = new ListNode(0);
        ListNode *head = node;
        int len = lists.size();
        bool flag = true;
        while (flag){
            int val = INT_MAX;
            int idx = 0;
            flag = false;
            for (int i = 0 ; i < len ; i ++){
                if ( lists[i] != NULL && lists[i]->val < val){
                    val = lists[i]->val;
                    idx = i;
                    flag = true;
                }
            }
            if (flag == false){
                break;
            }
            node->next = new ListNode(val);
            node = node->next;
            lists[idx] = lists[idx]->next;
        }
        return head->next;
    }
};