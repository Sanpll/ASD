import numpy as np


def count_less_mid(arr, n, mid):
    row, col = 0, n - 1
    count = 0
    while row < n and col >= 0:
        if arr[row][col] <= mid:
            count += (col + 1)
            row += 1
        else:
            col -= 1
    return count


def sorted_matrix(arr, k):
    n = arr.shape[0]
    left = arr[0][0]
    right = arr[n - 1][n - 1]

    while left < right:
        mid = (left + right) // 2
        if count_less_mid(arr, n, mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


def asserts():
    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
    assert sorted_matrix(arr, 7) == 7

    arr = np.array([[1, 2, 4, 7],
                    [3, 5, 8, 11],
                    [6, 9, 12, 14],
                    [10, 13, 15, 16]])
    assert sorted_matrix(arr, 7) == 7

    arr = arr * 2
    assert sorted_matrix(arr, 5) == 10


asserts()