import numpy as np
import time

start_time = time.time()


def maxContiguousSubarraySum(nums):
    n = len(nums)
    max_sum = -10000
    for left in range(0, n):
        print(left)
        for right in range(left, n):
            temp_sum = 0
            for k in range(left, right + 1):
                temp_sum += nums[k]
            max_sum = max(max_sum, temp_sum)
    return max_sum


np.random.seed(1069274)

random_numbers = np.random.randint(-100, 100, size=1000)

print(f"Max Contiguous Number found: {maxContiguousSubarraySum(random_numbers)}")
print("--- %s seconds ---" % (time.time() - start_time))
