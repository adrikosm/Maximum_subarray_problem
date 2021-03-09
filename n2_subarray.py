import numpy as np
import time

start_time = time.time()


def max_cont_array(nums):
    n = len(nums)
    max_sum = -1000
    actual_matrix = []
    for left in range(0, n):
        print(left)
        temp_sum = 0
        previous_sum = max_sum
        for right in range(left, n):
            temp_sum += nums[right]
            max_sum = max(max_sum, temp_sum)
        if max_sum > previous_sum:
            actual_matrix.append(max_sum)
    return actual_matrix


np.random.seed(1069274)

random_numbers = np.random.randint(-100, 100, size=100)
print(f"Max contiguous Number found: {max(max_cont_array(random_numbers))}")
print("--- %s seconds ---" % (time.time() - start_time))
