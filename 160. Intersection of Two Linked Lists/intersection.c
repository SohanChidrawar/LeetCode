/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *ptr1 = headA;
    struct ListNode *ptr2 = headB;
    int c1=0;
    int c2=0;
    while(ptr1!=NULL)
    {
        c1++;
        ptr1 = ptr1->next;
    }
    while(ptr2!=NULL)
    {
        c2++;
        ptr2 = ptr2->next;
    }
    int diff = abs(c1-c2);
    ptr1 = headA;
    ptr2=headB;

    if(c1>c2)
    {
        for(int i=1;i<=diff;i++)
            ptr1 = ptr1->next;
    }
    else
    {
        for(int j=1;j<=diff;j++)
            ptr2 = ptr2->next;
    }
    while(ptr1!=ptr2)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    return ptr1;
}
