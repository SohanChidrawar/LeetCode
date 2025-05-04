/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* a = list1;
    struct ListNode* b =list2;
    struct ListNode* first, *last;

    if(a == NULL)
        return list2;
    if(b==NULL)
        return list1;
    if(a->val < b->val)
    {
        last = first = a;
        a = a->next;
    }
    else
    {
        last = first = b;
        b = b->next;
    }

    while(a!=NULL && b!=NULL)
    {
        if(a->val < b->val)
        {
            last->next = a;
            last = a;
            a = a->next;
        }
        else
        {
            last->next = b;
            last = b;
            b = b->next;
        }
    }
    if(a!=NULL)
        last->next = a;
    if(b!=NULL)
        last->next = b;

    return first;
}
