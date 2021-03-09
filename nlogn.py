import numpy as np
import time

start_time = time.time()


def maxCrossingSum(array, left, mid, height):
    sum = 0
    left_sum = -10000
    for i in range(mid, left - 1, -1):
        print(i)
        sum = sum + array[i]
        if sum > left_sum:
            left_sum = sum
    sum = 0
    right_sum = -1000
    for i in range(mid + 1, height):
        print(i)
        sum += array[i]
        if sum > right_sum:
            right_sum = sum

    return max(left_sum + right_sum, left_sum, right_sum)


def maxSubArraySum(array, left, height):
    if left == height:
        return array[left]

    mid = (left + height) // 2

    return max(maxSubArraySum(array, left, mid),
               maxSubArraySum(array, mid + 1, height),
               maxCrossingSum(array, left, mid, height))


np.random.seed(1069274)

random_numbers = np.random.randint(-100, 100, size=100)
n = len(random_numbers)
left = 0
mid = int(n / 2)

print("Max Contiguous Number found ", maxCrossingSum(random_numbers, left, mid, n))
print("--- %s seconds ---" % (time.time() - start_time))
