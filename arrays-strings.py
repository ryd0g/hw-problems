# 1 Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

def find_largest(a, b):
    largest_nums = []
    for i in range(b):
        largest_value = max(a)
        largest_nums.append(largest_value)
        a.remove(largest_value)
    return largest_nums

print(find_largest([5, 1, 3, 6, 8, 2, 4, 7], 3))

# 2 Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]


def find_closest_sum_pair(a, b, t):
    a = sorted(a)
    b = sorted(b)
    a_index = 0
    b_index = len(b) - 1
    close_sum = None
    close_sum_a = None
    close_sum_b = None
    while a_index < len(a) and b_index >= 0:
        a_value = a[a_index]
        b_value = b[b_index]
        sum_value = a_value + b_value
        if close_sum is None or abs(sum_value - t) < abs(close_sum - t):
            close_sum = sum_value
            close_sum_a = a_value
            close_sum_b = b_value
        if sum_value > t:
            b_index -= 1
        elif sum_value < t:
            a_index += 1
        else:
            return [a_value, b_value]
    return [close_sum_a, close_sum_b]

print(find_closest_sum_pair([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20))