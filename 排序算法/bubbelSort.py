"""
排序是我们日常接触最多的问题，而排序算法也有很多很多。而冒泡排序就是我们排序算法的敲门砖
冒泡排序的思想很简单，就是从头开始，两两比较，让较大或较小的数向后移，就跟冒泡泡一样，依次将最大或最小数冒出来
冒泡排序因为只对自身进行排序操作，所以空间复杂度为O(1)。而时间复杂度则为O(n*n)
"""
import functools
import random
import time


# 打印执行时间帽子
def func_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time() * 1000
        res = func(*args, **kwargs)
        end = time.time() * 1000
        print(f'执行了: {end - begin}毫秒')
        return res
    return wrapper


@func_time
def bubble_sort(array):
    lenth = len(array)
    for i in range(lenth):
        for j in range(i+1, lenth):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(100)]
    bubble_sort(nums)
    print(nums)
