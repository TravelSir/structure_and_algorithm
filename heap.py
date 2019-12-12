"""
二叉树中有一种特殊形式叫完全二叉树，我们可以利用完全二叉树的特性和数组来实现二叉堆，而二叉堆一般用于实现优先队列
二叉堆可以通过自身调整，让最大或最小元素移动到顶点
二叉树数组就满足:
1. 父节点下标为x, 左子节点下标就为2x+1, 右子节点下标就为2x+2
2. 左子节点下标为x, 右子节点下标就为x+1, 那父节点的下标就是(x-1)/2,
3. 右子节点下标为x, 左子节点下标就为x-1, 那父节点的下标就是(x-2)/2
二叉堆一般有 插入节点，删除节点，构建二叉堆三种操作，这几种操作都基于堆的自我调整

1. 插入节点时，插入位置是完全二叉树最后一个位置，然后依次和父节点比较，以最小堆为例，如果值小于父节点，则新节点 上浮
2. 删除节点时，假设删除的是处于堆顶的节点，为了维持完全二叉树，将最后一个节点临时补充到堆顶，再和子节点比较，是否将节点 下沉
3. 构建二叉堆，也就是将一个无序的完全二叉树调整为二叉堆，本质就是让所有非叶子节点依次 下沉

上浮: 首先从最后一个叶子节点开始上浮，最后一个叶子节点坐标为x = len(n)-1, 父节点坐标为 (x-1)/2
下沉: 删除的节点，使用最后一个节点补上，然后再和子节点比较下沉
构建二叉堆: 就是不断下沉所有非叶子节点

最大优先队列中，无论入队顺序如何，当前最大的元素都会优先出队，这是基于最大堆实现的
最小优先队列中，无论入队顺序如何，当前最小的元素都会优先出队，这是基于最小堆实现的

"""


# 上浮
def up(heap, stype='min'):
    child = len(heap) - 1
    parent = (child - 1) // 2
    # 只需要记录上浮的节点的值即可，不用每次都互相交换，在上浮结束后一次赋值即可
    tem = heap[child]
    while child > 0 and ((tem < heap[parent] and stype=='min') or (tem > heap[parent] and stype=='max')):
        heap[child] = heap[parent]
        child = parent
        parent = (child - 1) // 2
    heap[child] = tem


# 下沉
def down(heap, index, stype='min'):
    tem = heap[index]
    child = 2 * index + 1
    lens = len(heap)
    while child < lens:
        # 先判断定位到左右孩子中最小或最大的那个
        if (child + 1 < lens and heap[child+1] < heap[child] and stype=='min') or (child + 1 < lens and heap[child+1] > heap[child] and stype=='max'):
            child += 1
        if (tem < heap[child] and stype=='min') or (tem > heap[child] and stype=='max'):
            break
        heap[index] = heap[child]
        index = child
        child = 2 * index + 1
    heap[index] = tem


# 构建二叉堆
def build(heap, stype='min'):
    leaf = (len(heap) - 2) // 2
    while leaf >= 0:
        down(heap, leaf, stype)
        leaf -= 1


# 优先队列
class PriorityQueue:
    def __init__(self, length=10, stype='min'):
        self.heap = []
        self.length = length
        self.stype = stype

    def add(self, num):
        if len(self.heap) == self.length:
            self.heap[0] = self.heap[-1]
            self.down()
            self.heap = self.heap[:-1]
        self.heap.append(num)
        self.up()

    def pop(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.down()

    def up(self):
        """上浮"""
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        tem = self.heap[child]
        while child > 0 and ((tem > self.heap[parent] and self.stype == 'max') or (tem < self.heap[parent] and self.stype == 'min')):
            self.heap[child] = self.heap[parent]
            child = parent
            parent = (child - 1) // 2
        self.heap[child] = tem

    def down(self):
        """下沉"""
        parent = 0
        child = parent * 2 + 1
        lens = len(self.heap)
        tem = self.heap[parent]
        while child < lens:
            if child + 1 < lens and ((self.heap[child + 1] > self.heap[child] and self.stype == 'max') or (self.heap[child + 1] < self.heap[child] and self.stype == 'min')):
                child += 1
            if (self.heap[child] > tem and self.stype == 'max') or (self.heap[child] < tem and self.stype == 'min'):
                self.heap[parent] = self.heap[child]
                parent = child
                child = parent * 2 + 1
            else:
                break
        self.heap[parent] = tem

    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    # a = [1, 3, 2, 6, 5, 7, 8, 9, 10]
    # up(a, 'max')
    # print(a)
    b = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    # build(b, 'max')
    # print(b)
    build(b, 'min')
    print(b)

    pr = PriorityQueue(stype='min', length=4)
    for i in b:
        pr.add(i)
    print(pr)
