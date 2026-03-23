def sort_stack(stack):
    dop_stack = []
    while len(stack) > 0:
        temp = stack.pop()
        len_unstacked = 0
        while len(dop_stack) > 0:
            if dop_stack[-1] > temp:
                stack.append(dop_stack.pop())
                len_unstacked += 1
            else:
                break

        dop_stack.append(temp)

        for i in range(len_unstacked):
            dop_stack.append(stack.pop())

    while len(dop_stack) > 0:
        stack.append(dop_stack.pop())

    return stack


def asserts():
    stack = [6, 4, 8, 1, 2, 3, 9, 5, 7, 0]
    assert sort_stack(stack) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    stack = []
    assert sort_stack(stack) == []

    stack = [4, 3, 2, 1]
    assert sort_stack(stack) == [4, 3, 2, 1]


asserts()