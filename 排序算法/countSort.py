"""
当数据是在一定范围内的整数，计数排序可以说是最快的排序，时间复杂度是线性的，但同时需要用空间换时间。
计数排序的原理是，找出序列最大和最小的数成为边界，创建一个对应的整数区间。将序列的数完全对应到区间内，再按区间顺序输出即可.
所以计数排序的时间复杂度是O（n+k），这个k取决于最大与最小值的差值
"""
import random


def count_sort(array):
    length = len(array)
    if length < 2:
        return array
    _min = _max = array[0]
    for i in array:
        if i < _min:
            _min = i
        if i > _max:
            _max = i
    tem = [0] * (_max - _min + 1)
    for n in array:
        tem[n - _min] += 1

    i = 0
    for n, cnt in enumerate(tem):
        while cnt > 0:
            array[i] = n + _min
            i += 1
            cnt -= 1


if __name__ == '__main__':
    nums = [random.randint(0, 100) for i in range(100)]
    count_sort(nums)
    print(nums)
