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
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ListNode* ptr = head;
        ListNode* temp = head;
        while(ptr != NULL){
            if (ptr->next != NULL){
                head = ptr;
                ptr = ptr->next;
                if (head->val == ptr->val){
                    head->next = ptr->next;
                    delete(ptr);
                    ptr = head;
                }
            }
            else{
                break;
            }
        }
        return temp;
    }

};