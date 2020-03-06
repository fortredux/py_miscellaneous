from random import randint

for_sum_list0 = [randint(1, 99) for i in range(6)]
for_sum_list1 = list.copy(for_sum_list0)
for_sum_list2 = list.copy(for_sum_list0)
for_sum_list3 = list.copy(for_sum_list0)
print(for_sum_list0)


def sum0(arr):
    if len(arr) == 0:
        return 0

    if len(arr) > 0:
        x = arr.pop(0)
        return x + sum0(arr)


# without recursion
def sum1(arr):
    sum = 0
    while len(arr) > 0:
        x = arr.pop(0)
        sum += x
    return sum


def sum2(arr, start=0):
    lenght = len(arr)

    if start == lenght:
        return 0

    if lenght != start:
        return arr[start] + sum2(arr, start=start+1)


# shorter version of sum2
def sum2_5(arr, start=0):
    lenght = len(arr)

    while lenght != start - 1:
        return arr[start] + sum2(arr, start=start+1)


print('sum0 = ' + str(sum0(for_sum_list0)))
print('sum1 = ' + str(sum1(for_sum_list1)))
print('sum2 = ' + str(sum2(for_sum_list2)))
print('sum2_5 = ' + str(sum2_5(for_sum_list3)))
