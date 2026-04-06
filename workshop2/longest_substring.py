def longest_substring(s: str):
    left = 0
    max_len = 0
    last_pos = {}

    for right, char in enumerate(s):
        if char in last_pos and last_pos[char] >= left:
            left = last_pos[char] + 1
        last_pos[char] = right

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len


def asserts():
    assert longest_substring("abcdebcghuiokl") == 11

    assert longest_substring("aaaaaaaa") == 1

    assert longest_substring("abcdefg") == 7


asserts()
