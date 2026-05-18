def lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def asserts():
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert lis(nums1) == 4

    nums2 = [1, 2, 3, 4, 5]
    assert lis(nums2) == 5

    nums3 = [5,4,3,2,1]
    assert lis(nums3) == 1

    nums4 = [2, 2, 2, 2]
    assert lis(nums4) == 1


asserts()