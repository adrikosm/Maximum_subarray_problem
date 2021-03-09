import numpy as np
import time

start_time = time.time()


def maxContiguousSubarraySum(nums, size):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, size):
        print(i)
        max_ending_here = max_ending_here + nums[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


np.random.seed(1069274)

random_numbers = np.random.randint(-100, 100, size=100)
size = len(random_numbers)
print(f"Max Contiguous Number found: {maxContiguousSubarraySum(random_numbers, size)}")
print("--- %s seconds ---" % (time.time() - start_time))
