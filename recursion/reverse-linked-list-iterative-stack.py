from stack import Stack

class ListNode:
    def __init__(self, payload = None, next: 'ListNode' = None) -> None:
        self.payload = payload
        self.next: 'ListNode' = next



def reverse_list(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    stack: Stack = Stack()

    while head is not None:
        stack.push(head)
        head = head.next

    dummy: ListNode = ListNode()
    dummy_tmp = dummy

    while not stack.is_empty():
        dummy_tmp.next = stack.pop()
        dummy_tmp = dummy_tmp.next

    dummy_tmp.next = None
    return dummy.next


    
