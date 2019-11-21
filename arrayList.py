# 数组
"""
数组是申请了一片连续的内存作为存储。
因为是连续的，所以我们只需要知道数组第一个元素所对应的内存地址，数组其他元素就可以通过第一个元素的内存地址加上下标，
就可以直接找到对应内存地址所存储的值。
所以a只是一个地址,所以无论a对应的数组有多大,在方法调用把a传参进去时都不会慢。
而正因为数组是申请的连续空间，所以数组的扩容就无法直接在原来的内存上往后伸长。因为内存上的数据会不断存储和释放，
所以内存是碎片化的存储，可能一个初始长度为5的数组要扩大到6的时候，原来存储的最后一个内存地址的下一个地址已经被使用了，
这样就无法保证连续性,所以此时是需要重新申请一个长度为6的内存来存数组。在python数组的扩充是自己方法实现了。
在使用像c之类的声明变量的语言时使用数组就需要根据实际情况初始化数组，太大了会浪费内存，太小了会不断的扩充内存，复制数据也很麻烦。
而且由于数组是顺序连续的,在进行插入删除操作的时候,需要把被被操作的元素后的所有元素往后或往前移。

数组的优点就是: 读取快
数组的缺点就是: 插入删除费时, 扩容时费时费内存

"""


# 基本的增删改查
import copy


def basic_opt(a):

    # 通过下标访问
    print(a[0])
    # 下标可为负数，表示倒数第几位
    print(a[-1])
    # 冷知识 bool值也可作为下标, True就是1, False就是0
    print(a[True], a[False])

    # 查找第一个匹配的元素位置
    # Tips:若元素不存在数组中会报错
    try:
        ind = a.index(1)
        print(ind)
        ind = a.index(2)
        print(ind)
    except ValueError as e:
        print(f'error: {e}')

    # 修改
    a[1] = 10
    print(a[1])

    # 插入
    a.insert(0, 0)
    print(a)

    # 数组末尾追加
    a.append(6)
    print(a)

    # 通过下标删除
    a.pop(2)
    print(a)

    # 删除制定元素
    # 同index不存在也会报错
    try:
        a.remove(0)
        print(a)
    except ValueError as e:
        print(f'error: {e}')


# 常用操作
def common_opt(a):
    # 排序 默认是正序从小到大
    a.sort()
    print(a)
    # 开启reverse倒序
    a.sort(reverse=True)
    print(a)
    # 甚至可以自定义排序规则,这里是大于3的数才排序
    a.sort(key=lambda x: x > 3)
    print(a)

    # 词频统计, 数组中1出现的次数
    print(a.count(1))

    # 清空数组
    a.clear()
    print(a)

    # 数组不仅可以添加一个元素，还可以添加可遍历的集合(对字典对遍历是key)
    b = (8, 8)
    c = [9, 9]
    d = {10: 1, 11: 2}
    a.extend(b)
    a.extend(c)
    a.extend(d)
    print(a)

    # 反转数组
    a.reverse()
    print(a)

    # 因为a其实是内存地址,我们要复制一个数组a，就不能直接用b=a，这样b和a其实都是指向同一片内存，a改了b也会一起改
    b = a
    print(b, a)
    a.append(8)
    print(b, a)
    # 所以如果我们要一个值和a一样的新数组,就要使用copy方法
    b = a.copy()
    a.append(9)
    print(b, a)
    # but! 虽然我们复制了a的值放到了一片新内存,但是由于数组是不仅仅能存变量的,也可以把数组,字典作为元素。
    # 所以数组里还有数组的话，那其实数组的值就有另一个数组的地址，所以虽然用copy方法将值重新存到另一片内存
    # 但复制过来的元素的地址和a里的地址指向的是另一个数组的同一内存

    c = [6, 6, 6]
    a.append(c)
    b = a.copy()
    a[-1].append(6)
    print(a, b, c)
    # 可以发现上面的c, a[-1], b[-1]都是指向同一块内存, 那如果我们要复制一个完全互不影响的数组
    # 就得在复制a的元素时，遇到值其实是地址的(其实也就是可迭代对象),将这个对象也copy一次，不断递归
    # 在python里实现这样方式的就是copy模块的deepcopy方法
    b = copy.deepcopy(a)
    c.clear()
    print(a, b)


# 切片
def arr_slice(a):
    # python中数组可以使用切片很方便的获取任意长度顺序的子区间
    # [x:y]取的是一个从下标x到下标y的左闭右开的区间
    print(a, a[1: 3])
    # [:]= [0: len(a) + 1] :前后不填时默认为0和length +1
    print(a[:], a[1:])
    # 切片也可使用负数
    print(a[:-2])

    # 切片还可设置步数,表示区间内从开头每一次走几步获得元素
    print(a[::2])
    # 其实我们平常用一个引号的切片其实就相当于设置步数为1的两冒号切片
    # 步数还可以设置负数,其实a.reverse = a[::-1]
    print(a[::-1])


if __name__ == '__main__':
    # 初始化数组
    arr = [1, 3, 2, 4, 5, 1, 3, 1]
    basic_opt(arr)
    common_opt(arr)
    arr_slice(arr)

