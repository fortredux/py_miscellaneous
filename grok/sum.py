for_sum_list = [1, 4, 8, 20, 50]


def sum(arr):
    if len(arr) == 0:
        return 0

    if len(arr) > 0:
        x = arr.pop(0)
        return x + sum(arr)


print(sum(for_sum_list))
