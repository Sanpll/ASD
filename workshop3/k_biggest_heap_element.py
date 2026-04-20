import heapq


def k_biggest_heap_element(data: list, k: int):
    if len(data) <= k or k < 1:
        raise ValueError

    k_heap = []
    for element in data:
        if len(k_heap) < k:
            heapq.heappush(k_heap, element)
        else:
            heapq.heappushpop(k_heap, element)

    return heapq.heappop(k_heap)


def asserts():
    assert k_biggest_heap_element([3, 2, 1, 5, 6, 4], 3) == 4
    assert k_biggest_heap_element([1, 1, 2, 2, 3, 3, 4, 4], 5) == 2

    try:
        k_biggest_heap_element([3, 2, 1, 5, 6, 4], 10)
    except ValueError:
        assert True
    except Exception:
        assert False
    else:
        assert False


asserts()
