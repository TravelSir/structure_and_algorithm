"""
栈的特点是先进后出，后进先出。
队列的特点是先进先出，后进后出。
栈和队列既可以用数组也可以用链表实现
"""
import queue


# 自定义栈
from collections import deque


class Stack:

    def __init__(self):
        self.array = []

    # 入栈
    def add(self, n):
        self.array.append(n)

    # 出栈
    def pop(self):
        try:
            tem = self.array[-1]
            self.array = self.array[:-1]
            return tem
        except ValueError as e:
            print(e)

    # 自定义string返回
    def __repr__(self):
        return str(self.array)


# 自定义队列
class Queue:

    def __init__(self):
        self.array = []

    # 入队
    def add(self, n):
        self.array.append(n)

    # 出队
    def pop(self):
        try:
            tem = self.array[0]
            self.array = self.array[1:]
            return tem
        except ValueError as e:
            print(e)

    # 自定义string返回
    def __repr__(self):
        return str(self.array)


if __name__ == '__main__':
    stack = Stack()
    stack.add(1)
    stack.add(2)
    print(stack)
    print(stack.pop(), stack)

    que = Queue()
    que.add(1)
    que.add(2)
    print(que)
    print(que.pop(), que)

    """
    其实我们可以发现其实python自带的数组就有append方法和pop方法，其实完全就满足了栈的要求
    
    栈可以直接用数组，那为什么队列会有一个专门的模块queue呢

    首先栈使用数组实现，当比如长度为10的栈，出栈一次，其实并没有释放第10个内存，只是有一个尾指针标记栈在数组的哪个地方结束，
    而再入栈的时候，只需要覆盖第10个内存的值，再移动尾指针到第10，这样的话对内存实现了高复用性，不用频繁的去申请新内存，减少内存开销。

    而队列因为出队是出的头，那比如长度为10的队列，出队一次，头指针来标记队列从哪开始，头指针就向后移一位，但入队还是尾部增加，
    所以这样随着不断的出队，前面的内存会不断的空出来，所以为了复用内存，所以还需要一个尾指针来标记结束位置，而当后面的内存满了后，
    队列就会在前面的内存上开始存储，尾指针也会移动到前面，可能在数组里尾指针会在头指针前面了。

    而当栈和队列的内存都满了后，数组再扩容，栈只需要将原内存的值顺序复制到新内存就行了，或者如果原内存后还有可用的连续内存，直接使用后面的内存即可
    但队列扩容，就无法向栈一样直接复制或向后加，需要重新排序，原来可能尾指针在头指针前，扩容后应该是头指针在内存头，尾指针在后面。

    所以栈但扩容就和数组扩容一样，但队列扩容就得特殊处理，所以python内置一个专门的queue模块。但内置但queue模块不只做这些事，它还实现了中间件的功能
    """
    # 优化栈 = 数组
    a = list()
    a.append(1)
    print(a)
    print(a.pop(), a)

    # 优化队列 = 内置queue模块
    # 其实内置的queue模块是用deque双端队列来实现的，双端队列其实就是结合了栈和队列的特点，既可以先进先出，也可以后进后出
    b = queue.Queue()
    b.put(1)
    b.put(2)
    print(b.get())
    print(b.get())

    # 双端队列
    deq = deque([1, 2, 3])
    deq.append(4)
    print(deq.pop(), deq.popleft())
