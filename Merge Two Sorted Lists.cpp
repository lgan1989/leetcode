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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ListNode* node = new ListNode(0);
        ListNode* head = node;
        while (true){
            if (l1 == NULL && l2 == NULL)break;
            else if (l1 == NULL){
                node->next = new ListNode(l2->val);
                l2 = l2->next;
                node = node->next;
            }
            else if (l2 == NULL){
                node->next = new ListNode(l1->val);
                l1 = l1->next;
                node = node->next;
            }
            else{
                int v = min(l1->val , l2->val);
                node->next = new ListNode(v);
                if (l1->val < l2->val){
                    l1 = l1->next;
                }
                else{
                    l2 = l2->next;
                }
                node = node->next;
            }
        }
        return head->next;
    }
};