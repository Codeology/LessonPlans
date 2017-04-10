public ListNode removeElements(ListNode head, int val) {
  while(head != null && head.val == val) {
      head = head.next;
  }
  if(head == null) {
      return head;
  }
  ListNode p = head;
  while(p.next != null) {
      if(p.next.val == val) {
          p.next = p.next.next;
      } else {
          p = p.next;
      }
  }
  return head;
}
