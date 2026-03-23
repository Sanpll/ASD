class MyNode:
    def __init__(self, value: int, nxt=None):
        self.value = value
        self.next = nxt


def two_linked_lists(head1: MyNode, head2: MyNode):
    iter1 = head1
    iter2 = head2
    while iter1 is not None or iter2 is not None:
        if iter1 is iter2:
            return iter1
        elif iter1 is None:
            iter1 = head2
        elif iter2 is None:
            iter2 = head1
        iter1 = iter1.next
        iter2 = iter2.next
    return None


def asserts():
    head = MyNode(5)
    head = MyNode(4, head)
    head = MyNode(8, head)
    head = MyNode(1, head)

    head_a = MyNode(4, head)

    head_b = MyNode(6, head)
    head_b = MyNode(5, head_b)

    head_c = MyNode(5)
    head_c = MyNode(4, head_c)
    head_c = MyNode(8, head_c)
    head_c = MyNode(1, head_c)

    assert two_linked_lists(head_a, head_b) is head
    assert two_linked_lists(head_a, head_c) is None


asserts()
