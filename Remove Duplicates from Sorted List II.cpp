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
    ListNode *deleteDuplicates(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode* ans = new ListNode(0);
        ans->next = head;
        ListNode* pre = ans;
        while (head != NULL){
            ListNode* next = head->next;

            bool flag = false;
            while (next != NULL && head->val == next->val){
                next = next->next;
                flag = true;
            }
            if (flag){
                pre->next = next;
                head = pre->next;
            }
            else{
                pre = head;
                head = head->next;
            }
        }
        return ans->next;
    }
};