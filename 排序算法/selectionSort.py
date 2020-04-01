"""
选择排序是一个时间复杂度稳定为O(n*n)的算法。它的思想就是在未排序的序列中找到最大或最小的数放在序列起始位置，再继续在剩余未排序序列中找出最大或最小数，
放在已排序序列末尾。以此类推。而为了找出最大或最小数，只需要一个临时变量，所以空间复杂度是O(1)

"""
import random


def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        _min = i
        for j in range(i + 1, length):
            if array[_min] > array[j]:
                _min = j
        array[_min], array[i] = array[i], array[_min]


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(100)]
    selection_sort(nums)
    print(nums)
