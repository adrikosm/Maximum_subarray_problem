import numpy as np
import time

start_time = time.time()


def maxContiguousSubarraySum(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far


np.random.seed(1069274)

random_numbers = np.random.randint(-100, 100, size=100)
print(f"Max Contiguous Number found: {maxContiguousSubarraySum(random_numbers)}")
print("--- %s seconds ---" % (time.time() - start_time))
