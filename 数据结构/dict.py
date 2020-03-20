"""
在python中的dict是以键值对的形式存在的，我们可以根据key非常快速的找到对应的value，那这是怎么实现的呢
其实dict就是散列表，跟java中的HashMap一样，也叫哈希表，查找的时间复杂度接近于O(1)
在数组中，我们通过下标访问，其实就是根据头地址计算出了对应的内存地址，从而很快速的找到对应的值，其实散列表也是通过数组来实现的。

在大多数面向对象的语言中，每一个对象都有属于自己的hashcode用来区分不同对象，无论对象本身是什么类型，它的hashcode都是一个整型
那既然是整型，我们就可以转为数组的下标使用。比如我们一个key为'this'的字符串，我们首先对它进行hash算出this字符串对应的hashcode值，
但是这个值可能会很大，超出数组的边界怎么办，所以我们需要对hashcode值进行数组长度的取模(求余)操作,再存入对应的数组下标位置就可以了

但是这样肯定会出现问题，那就是两个不同hash值的对象它们取模过后的值是一样的，那它们不就在数组同一个地方冲突了吗？这其实就是哈希冲突
为了解决哈希冲突，有一种方法是开放寻址法。基本思路是，当取模后找到对应的数组下标，发现已经存在值了，那就会寻找改下标相邻的空内存存储
而取值的时候也是这样，当找到对应下标的key和要查询的key对不上的时候，它会去该下标附近寻找。当然寻址方法有很多种，这只是一个简单的示例。

在jdk8以前的版本的HashMap其实使用了另一种方法: 链表法 (最新的java中其实用的是红黑树)
当key哈希取模后找到对应的数组下标发现已经存在其他key的值了，这个时候其实数组里存的数据是 key, value, next三个,
key用来检验是不是同一key,有没有产生哈希冲突。 value是真正对应的值。 而next则是当有hash冲突时，这是一个链表的指针，指向下一个节点来存储冲突的key和value

散列表就是这样巧妙的将数组和链表同时使用起来达到了高效的键值对映射关系的查询。

前面我们说散列表的时间复杂度接近O(1), 其实就是在哈希不冲突的时候是1，但冲突了就得看链表的长度了。当数组饱和时需要扩容，散列表肯定也要。
而扩容后因为长度变了，对所有对象要重新hash再分布。
"""


# 链表法实现一个简单字典
class Dict:
    def __init__(self, length=10):
        # 这里假设数组长度为10
        self.length = length
        self.array = [None for i in range(length)]

    # 实现下标访问
    def __getitem__(self, key):
        """ x.__getitem__(y) <==> x[y] """
        return self.get(key)

    # 实现下标设值
    def __setitem__(self, key, value):
        """ Set self[key] to value. """
        return self.add(key, value)

    def add(self, key, value):
        hash_code = hash(key)
        # 这里假设数组长度为10
        index = hash_code % self.length
        node = self.array[index]
        # 未哈希冲突
        if node is None:
            self.array[index] = DictNode(key, value)
        # 有哈希冲突
        else:
            while node:
                # 已存在则覆盖值
                if node.key == key:
                    node.value = value
                    break
                # 未存在则添加到链表最后
                if not node.next:
                    node.next = DictNode(key, value)
                node = node.next

    def get(self, key):
        hash_code = hash(key)
        index = hash_code % self.length
        node = self.array[index]
        if node is None:
            return node
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return node


class DictNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


if __name__ == '__main__':
    d = Dict()
    print(d.get('test'))
    d['test'] = "it's ok"
    print(d['test'])
    d['test'] = "it's changed"
    print(d['test'])

    # 由于哈希值每次运行是随机的(猜测跟每次随机分配的内存地址有关)，所以为了测试我们将数组大小设置到2,设置3个值
    print(hash('test1') % 2, hash('test2') % 2, hash('test3') % 2)
    di = Dict(2)
    d['test1'] = 'i am one'
    d['test2'] = 'i am two'
    d['test3'] = 'i am three'
    print(d['test1'], d['test2'], d['test3'])


