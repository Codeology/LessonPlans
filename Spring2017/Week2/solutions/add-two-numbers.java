public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode start = new ListNode(0);
    ListNode p = start;
    int v1, v2, remainder = 0;
    while (l1!=null || l2!=null || remainder > 0) {
        v1 = l1==null? 0: l1.val;
        v2 = l2==null? 0: l2.val;
        remainder += v1 + v2; // keep building on top of remainder
        p.next = new ListNode(remainder%10);
        remainder /= 10;
        p = p.next;
        if (l1!=null) l1 = l1.next;
        if (l2!=null) l2 = l2.next;
    }
    return start.next;
}
