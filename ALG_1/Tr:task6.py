import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)

    l_nums = [i for i in nums if i < q]
    m_nums = [q]*nums.count(q)
    r_nums = [i for i in nums if i > q]

    return quicksort(l_nums) + m_nums + quicksort(r_nums)


arr = list(map(int, input().split()))
arr = quicksort(arr)
max1 = arr[-1]*arr[-2]*arr[-3]
max2 = arr[0]*arr[1]*arr[-1]
if max2 > max1:
    print(arr[0], arr[1], arr[-1])
else:
    print(arr[-1],arr[-3], arr[-2])