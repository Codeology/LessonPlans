public boolean isPalindrome(ListNode head) {
    if (head==null || head.next==null) return true;
    Stack<Integer> stack = new Stack<>();
    ListNode pointer = head;
    while (pointer!=null) {
        stack.push(pointer.val);
        pointer = pointer.next;
    }
    while (head!=null) {
        if (head.val!=stack.pop()) return false;
        head = head.next;
    }
    return true;
}
