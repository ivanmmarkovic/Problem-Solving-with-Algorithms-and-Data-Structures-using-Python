
class ListNode: 
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode)->ListNode:
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        next: ListNode = head.next
        head.next = None
        rest: ListNode = reverse_list(next)
        next.next = head
        return rest