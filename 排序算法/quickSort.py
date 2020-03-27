"""
如果说冒泡排序是排序算法的敲门砖，那么快排就是排序算法的地基。快排基本上可以解决我们遇到的百分之九十的工作需求和问题，当然各个语言也是内置了快排函数的
快排的思想是分治法的一种实现。分治法的思想就是把一个规模为n的问题，拆分成k个规模较小的问题，这些子问题相互独立且与原问题性质相同，通过合并子问题的解得出原问题的解
快排的方法就是，每一轮选一个基准元素，让比它大的数排在右边，比它小的数排在左边，从而把数组拆成两个数组。然后再不断的往下拆，直到不能在拆分。
这样每一轮遍历的元素依旧是n个，但遍历的轮数就减少到了log(n)次，所以快排的时间复杂度是O(n*log(n))。
而怎么选基准元素呢，如果我们每次都选择第一个元素作为基准元素，那么在一个数组完全逆序的情况下，那么轮次就会增加到n次，所以基准元素的选取一般是随机的。
那如何把大的元素都放在右边，小的元素都放在左边呢，这里的元素交换实现有两种方法: 单边循环法和双边循环法
- 双边循环法就是设定一个左指针和右指针分别指向数组的两端，因为要让数组右边都是大于基准元素的。所以我们先从右指针所指向的数开始判断
    如果右指针所指的数大于等于基准数，那么这个数的位置肯定就不用变了，那么右指针可以左移一位，继续判断
    如果右指针所指的数小于基准数，说明这个数应该在左边的数组，那么这个时候转为判断左指针
        - 假设左指针指的数小于等于基准数，那么说明这个数本来就应该在左边，所以这个数位置就不用变。左指针就向右移一位，继续判断
        - 假设左指针指的数大于基准数，那么说明这个数应该在右边的数组，所以这个时候可以把左右指针的数交换，然后左右指针都同时移动一位
  当左右指针相等时，那就说明这个点是左边小数组和右边大数组的分割点，也就是排序后的基准数的位置，最后这里就交换这个点和原基准数的位置

- 双边循环法虽然更加直观，但代码实现相对复杂，而单边循环法则简单的多
    首先设置一个指针p，指向数组左边界。这个指针表示排序后左右数组的分解点。所有小于基准数的数都应该在p指针左边。初始默认所有数都大于基准数
    从第一个数开始，依次和基准数比较
    - 如果这个数比基准数小，那么说明分割点要往右移一位，所以p指针指向的数和这个数交换，然后p指针向右移一位
    最后遍历完成后，将p指针对应的数和基准数交换即可

单双边循环法只是确定如何拆分问题，那如何把所有问题的结果组合起来呢，我们可以用递归和栈两种方式。
其中递归利于理解，但本身消耗调用栈，很消耗内存。所以最好还是用栈。
"""
import copy
import random


from 排序算法.bubbelSort import cocktail_sort
from 排序算法.util import func_time


# 双边循环法 + 递归
def quick_sort(array, begin=None, end=None):

    if begin is None:
        begin = 0
    if end is None:
        end = len(array) - 1
    if end <= begin:
        return
    left, right = begin, end
    pivot_index = left
    pivot = array[pivot_index]  # 基准数下标
    order = True  # 顺序
    while left < right:
        if order:
            if array[right] < pivot:
                order = False
            else:
                right -= 1
        else:
            if array[left] > pivot:
                array[left], array[right] = array[right], array[left]
                right -= 1
                order = True
            else:
                left += 1
    array[pivot_index], array[left] = array[left], array[pivot_index]

    quick_sort(array, begin, left)
    quick_sort(array, left + 1, end)


@func_time
# 单边循环法 + 栈
def quick_sort_better(array, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(array)
    stack = list()
    stack.append([begin, end])

    while stack:
        _array = stack.pop()
        begin, end = _array[0], _array[1]
        pivot_index = begin
        pivot = array[pivot_index]  # 基准数下标
        p = begin  # 临界点
        for i in range(begin + 1, end):
            if array[i] < pivot:
                p += 1
                array[p], array[i] = array[i], array[p]
        array[pivot_index], array[p] = array[p], array[pivot_index]
        if p > begin + 1:
            stack.append([begin, p])
        if p < end - 1:
            stack.append([p+1, end])


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(100)]
    nums2 = copy.deepcopy(nums)
    quick_sort(nums)
    quick_sort_better(nums2)
    print(nums)

    # 来对比一下冒泡和快排的时间差距
    nums3 = [random.randint(0, 1000) for i in range(1000)]
    nums4 = copy.deepcopy(nums3)
    print('冒泡排序时间:', end='')
    cocktail_sort(nums3)
    print('快速排序时间:', end='')
    quick_sort_better(nums4)
