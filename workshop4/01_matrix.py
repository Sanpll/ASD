def matrix_dp(mtx):
    m, n = len(mtx), len(mtx[0])
    dist = [[float("inf")] * n for _ in range(m)]

    # Первый проход: сверху-влево
    for i in range(m):
        for j in range(n):
            if mtx[i][j] == 0:
                dist[i][j] = 0
            else:
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

    # Второй проход: снизу-вправо
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i < m - 1:
                dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
            if j < n - 1:
                dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

    return dist


def asserts():
    mtx1 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    expected1 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1]
    ]
    assert matrix_dp(mtx1) == expected1

    mtx2 = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    expected2 = [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ]
    assert matrix_dp(mtx2) == expected2


asserts()