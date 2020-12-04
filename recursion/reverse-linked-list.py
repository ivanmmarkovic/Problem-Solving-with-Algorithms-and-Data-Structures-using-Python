class ListNode:
    def __init__(self, val: int = None, next = None):
        self.val = val
        self.next = next


def reverse_linked_list(node: ListNode) -> ListNode:
    if node is None:
        return None
    elif node.next is None:
        return node
    else:
        next_node: ListNode = node.next
        node.next = None
        rest: ListNode = reverse_linked_list(next_node)
        next_node.next = node
        return rest

