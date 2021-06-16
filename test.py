
# 快排: 每次遍历以第一个数作为基准数，把小于和大于基准数的数分别排两边，这里以增序为例
# 快排有两张循环方式：双边循环和单边循环
from typing import List


# 双边循环 + 递归
# 双边循环的思想就是从右开始找第一个小数，再从左边找第一个大数，再交换这两个数，最后要停留在小于基数的数，再交换基准数
def quick_sort(array: List[str], begin=None, end=None):
    if begin is None and end is None:
        begin = 0
        end = len(array) - 1
    if begin >= end:
        return

    pivot = begin  # 选定基准数为第一个数
    left, right = begin, end  # 递归需保留begin和end的值

    order = True  # True为从右开始找, False为从左开始找
    while left < right:
        if order:
            # 找到小于基数的数
            if array[right] < array[pivot]:
                order = False
            else:
                right -= 1
        else:
            # 找到大于基数的数
            if array[left] > array[pivot]:
                array[left], array[right] = array[right], array[left]
                right -= 1
                order = True
            else:
                left += 1

    array[pivot], array[right] = array[right], array[pivot]

    quick_sort(array, begin, left-1)  # 继续遍历左区间
    quick_sort(array, left+1, end)  # 继续遍历右区间
    return


# 单边循环 + 栈
# 单边循环的思想就是确定小数边界
def quick_sort_singe(array: List[str]):

    stack = list()
    stack.append([0, len(array) - 1])

    while stack:
        _array = stack.pop()
        begin, end = _array[0], _array[1]
        mark = pivot = begin
        for i in range(begin + 1, end + 1):
            if array[i] < array[pivot]:
                mark += 1
                array[mark], array[i] = array[i], array[mark]
        array[mark], array[pivot] = array[pivot], array[mark]

        if begin < mark - 1:  # mark的位置已经确定了就不用排了
            stack.append([begin, mark])
        if mark + 1 < end:
            stack.append([mark+1, end])


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    quick_sort_singe(nums)
    print(nums)
