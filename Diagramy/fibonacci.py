import time


def fib(limit, get_time=False, only_last=False):
    i = 1
    nums = [1, 2]
    a, b = 1, 2
    if limit == 1:
        return 1
    seconds = time.time()
    while i < limit - 1:
        a, b = b, a + b
        nums.append(b)
        i += 1
    if only_last:
        nums = nums[len(nums) - 1]
    if get_time:
        return nums, time.time() - seconds
    return nums


print(fib(1000, only_last=True))