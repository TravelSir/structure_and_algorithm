"""
插入排序，又名扑克排序。它的思想很容易理解, 打过扑克的都知道，桌上的牌组是被随机打乱的，但一张一张摸到自己手上的时候，后摸的牌会在手上已排序的牌组中找到对应的位置插入进去
它的实现跟选择排序很像。都是前后分成已排序和未排序的两部分。选择排序是从未排序中依次选择最小或最大的数加到已排序数组后。而插入排序是选择未排序数组中的第一个数，
去和已排序数组中的数比较插入。因为我们要实现线性的内存复杂度，所以需要操作自身，那插入位置后的数得依次后移。所以我们插入的时候需要从已排序数组末尾开始比较，
有点像冒泡一样，依次交换冒到自己的位置。这样在插入到对应位置时，插入位置后的数已经依次后移了
"""
import random


def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if array[j] > array[j-1]:
                break
            array[j], array[j-1] = array[j-1], array[j]


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(100)]
    insert_sort(nums)
    print(nums)

