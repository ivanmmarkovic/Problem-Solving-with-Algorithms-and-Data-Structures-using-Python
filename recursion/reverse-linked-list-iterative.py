class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    stopped: bool = False
    prev = head.next
    head.next = None
    while not stopped:
        tmp: ListNode = prev.next
        prev.next = head
        head = prev
        if tmp is not None:
            prev = tmp
        else:
            stopped = True

    return prev
