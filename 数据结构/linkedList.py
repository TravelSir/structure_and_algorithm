"""
链表:
链表与数组不同,链表在内存中是非连续的
链表头元素与数组头元素一样,存了本身的值和地址。由于链表不是连续的,所以第二个元素使用地址+1的方式就会找错.
所以链表每一个元素还会存后面的元素的地址。所以在读取元素的时候，我们只能从链表头元素依次读下去,而不能像数组那样
但是由于链表不需要连续内存，所以链表的扩容很容易。而且在进行插入删除操作时，只需要操作相邻的链表元素即可

链表的优点是: 插入删除快, 扩容方便
链表的缺点是: 读取很慢
"""


# 链表结构需要我们自己实现，这里是一个单向链表
class Linked:
    def __init__(self, data):
        self.data = data
        self.nex = None


def print_link(head):
    """打印链表值"""
    while head is not None:
        print(head.data, end=' ')
        head = head.nex
    print()


def basic_opt(head):
    """基本操作"""
    link = head
    # 访问链表第3个节点
    for i in range(1, 3):
        head = head.nex
    print(head.data)

    # 在链表第3个节点后插入一个节点
    node = Linked(0)
    _tem = head.nex
    head.nex = node
    node.nex = _tem
    print_link(link)

    # 删除第4个节点，只需要把第3个节点的指针指向第5个节点即可
    head.nex = head.nex.nex
    print_link(link)


if __name__ == '__main__':
    # 初始化一个链表
    tem = link = Linked(1)
    for i in range(2,6):
        nex = Linked(i)
        tem.nex = nex
        tem = tem.nex

    print_link(link)

    basic_opt(link)

