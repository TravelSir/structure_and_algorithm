"""
排序是我们日常接触最多的问题，而排序算法也有很多很多。而冒泡排序就是我们排序算法的敲门砖
冒泡排序的思想很简单，就是从头开始，两两比较，让较大或较小的数向后移，就跟冒泡泡一样，依次将最大或最小数冒出来
冒泡排序因为只对自身进行排序操作，所以空间复杂度为O(1)。而时间复杂度则为O(n*n)

当排序的数组本身就是有序的时候，其实我们第一遍遍历是没有任何元素交换的，这其实就不需要再进行接下来的遍历了
因为假设数组是[a, b, c, d], 没有交换操作的话, a<=b, b<=c, c<=d, 那a<=b<=c<=d. 已经判断出有序了
所以冒泡排序的优化算法是记录当次循环是否交换了元素, 如果没有交换, 说明已经有序了.

优化后的冒泡排序的条件是在一次循环中都没有交换过元素，说明这一段数据已经有序了。那比如这段数据前半段是无序的，后半段其实是有序的呢
例如: 3,4,2,1,5,6,7,8
在我们进行第一次冒泡的时候，2,1会交换，然后继续判断到末尾，都没有交换，这说明在2，1位置后面的数据已经有序了，那下一次循环就无需再判断了。
这就是我们冒泡排序的优化版2.0 我们记录下最后一次交换的位置，因为2，1后面是有序的，
而2，1交换后也是有序的，所以最后一次交换的位置就是交换前2的位置，作为下一次遍历的边界。

优化后的冒泡排序针对的是后半段是有序的数组的优化，那前半段是有序的呢
例如: 2,3,4,5,6,7,8,1
因为我们的遍历是从左往右，所以虽然2,3,4,5,6,7,8是有序的，但我们依然要依次判断到最后交换8 1、7 1、6 1,
其实前面的遍历其实就是浪费了的，所以既然从左往右是浪费了的，那我可以从右往左遍历呀。这就是鸡尾酒算法。
为什么叫鸡尾酒算法，因为鸡尾酒就是不断的从左边往右边倒，再从右边往左边倒来混合，就跟这个算法很形象
"""
import copy
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


# 简单冒泡排序
@func_time
def bubble_sort(array):
    lenth = len(array)
    for i in range(lenth - 1):
        for j in range(lenth - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# 优化冒泡排序1.0
@func_time
def bubble_sort_optimize(array):
    lenth = len(array)
    for i in range(lenth - 1):
        flag = True
        for j in range(lenth - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
        if flag:
            return


# 优化冒泡排序2.0
@func_time
def bubble_sort_optimize_v2(array):
    lenth = len(array)
    end = lenth - 1
    for i in range(lenth - 1):
        flag = True
        _end = end
        for j in range(end):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
                _end = j
        end = _end
        if flag:
            return


# 鸡尾酒排序
@func_time
def cocktail_sort(array):
    lenth = len(array)
    order = True  # 标记正序遍历还是逆序遍历
    for i in range(lenth-1):
        flag = True
        # 正序遍历
        if order:
            for j in range(lenth - 1 - i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = False
        else:
            for j in range(lenth - 1 - i, 0, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                    flag = False
                    
        order = order is False
        if flag:
            return


TEST_DATE = {
    'random': [random.randint(0, 100) for i in range(1000)],  # 随机
    'positive': [i for i in range(1000)],  # 完全正序
    'end_positive': [random.randint(0, 500) for i in range(500)] + [i for i in range(500, 1000)],  # 后部分正序
    'front_positive': [i for i in range(500)] + [random.randint(500, 1000) for i in range(500)],  # 前部分正序
}

if __name__ == '__main__':
    for k in TEST_DATE:
        print(f'数据是{k}的')
        nums = TEST_DATE[k]
        nums2 = copy.deepcopy(nums)
        nums3 = copy.deepcopy(nums)
        nums4 = copy.deepcopy(nums)
        print(f'排序前: {nums}')

        print('基础冒泡排序', end='')
        bubble_sort(nums)
        # print(f'排序后{nums}')

        print('优化冒泡排序', end='')
        bubble_sort_optimize(nums2)
        # print(f'排序后{nums2}')

        print('优化冒泡排序v2', end='')
        bubble_sort_optimize_v2(nums3)
        # print(f'排序后{nums3}')

        print('鸡尾酒排序', end='')
        cocktail_sort(nums4)
        print(f'排序后{nums4}')

        print()
