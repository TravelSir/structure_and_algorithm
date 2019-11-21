"""
栈和队列都是线性关系，但有许多逻辑关系类似 皇帝-多位大臣-多位官员 这样一对多甚至是多对多的非线性关系。而树和图就是这样的结构

树其实就是一对多的关系，树的特点是:
1. 有且只有一个根节点
2. 每一个子节点包含它的所有子节点的集合是它父节点的子树
3. 树的最大层级就是它的深度
4. 没有任何节点的树为空树
5. 没有任何子节点的节点叫做叶子节点

树结构中我们最常用的是二叉树。二叉树即一个父节点最多只能有两个子节点。而根据二叉树的特点，一般我们使用的是链表来实现。但二叉堆是用数组来实现的
二叉树中还有两种特殊形式:
1. 满二叉树: 一个二叉树的所有非叶子节点都有左右两个子节点,且所有叶子节点在同一层级上
2. 完全二叉树: 对于一个有n个节点的二叉树，按层级顺序编号，则所有节点的编号为从1到n。如果这个树所有节点和深度同样省督的满二叉树的编号从1到n的编号
位置完全相同，那么这个二叉树为完全二叉树。

二叉树有很多特殊形式，每一种形式都有其特别的作用，但最主要的应用还是在查找和排序上
最常用的一个就是二叉查找树(也叫二叉排序树): 左子树小于父节点, 右子树大于父节点。
但可能由于数据的问题导致查找树结构疯狂往一边偏斜，使深度大大增加。所以为了避免偏斜，就需要二叉树的自平衡。而自平衡的方式就有很多:红黑树,AVL树,树堆等等

由于二叉树是一个非线性的结构，所以对于二叉树的遍历有多种方式:
1. 前序遍历: 遍历的顺序是根节点-左子树-右子树
2. 中序遍历: 遍历的顺序是左子树-根节点-右子树
3. 后序遍历: 遍历的顺序是左子树-右子树-根节点
4. 层序遍历: 遍历的顺序是从第一层开始把每一层从左到右遍历完再到下一层继续遍历

其实遍历的方式从广义上分的话:
1. 深度优先遍历(DFS): 像打桩机一样优先往深处走, 包括前序，中序，后序遍历方式
2. 广度优先遍历(BFS): 像推土机一样优秀推平上层, 也就是层序遍历
"""


# 二叉树链表实现
class TreeNode:

    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
        self.flag = False


# 递归DFS
def dfs(node, model='front'):
    if node is None:
        return list()

    # 中序遍历
    if model == 'middle':
        return middle_traverse(node)

    # 后序遍历
    elif model == 'end':
        return end_traverse(node)

    # 前序遍历
    else:
        return front_traverse(node)


# 递归BFS = 层序遍历
def bfs(node, result=None):
    if node is None:
        return list()
    if result is None:
        result = [node.data]
    if node.left:
        result.append(node.left.data)
    if node.right:
        result.append(node.right.data)
    if node.left:
        result = bfs(node.left, result)
    if node.right:
        result = bfs(node.right, result)
    return result


# 前序遍历
def front_traverse(node, result=None):
    if result is None:
        result = list()
    result.append(node.data)
    if node.left:
        result = front_traverse(node.left, result)
    if node.right:
        result = front_traverse(node.right, result)
    return result


# 中序遍历
def middle_traverse(node, result=None):
    if result is None:
        result = list()
    if node.left:
        result = middle_traverse(node.left, result)
    result.append(node.data)
    if node.right:
        result = middle_traverse(node.right, result)
    return result


# 后序遍历
def end_traverse(node, result=None):
    if result is None:
        result = list()
    if node.left:
        result = end_traverse(node.left, result)
    if node.right:
        result = end_traverse(node.right, result)
    result.append(node.data)
    return result


# 当树节点足够多的时候，使用递归会造成堆栈溢出，python默认递归次数最大是1000，可以通过sys.setrecursionlimit(n)方法来设置更大值。
# 所以绝大多数递归都能使用栈来替代，因为递归和栈都有回溯的特性
def stack_dfs(node, model='front'):
    result = []
    if node is None:
        return result
    stack = []
    if model == 'middle':
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                tem = stack.pop()
                result.append(tem.data)
                node = tem.right

    elif model == 'end':
        # 后序遍历使用栈遍历会比前序和中序要难很多。需要标记节点是否遍历完右子树
        stack.append(node)
        while stack:
            if node and not node.flag:
                while node:
                    tem = None
                    if node.right:
                        stack.append(node.right)
                        tem = node.right
                    if node.left:
                        stack.append(node.left)
                        tem = node.left
                    node.flag = True
                    node = tem
            if stack:
                node = stack.pop()
                # 在遇到没有遍历完右子树的节点时，我们还要把它塞回栈
                if node.flag:
                    result.append(node.data)
                else:
                    stack.append(node)
    else:
        while node or stack:
            while node:
                stack.append(node)
                result.append(node.data)
                node = node.left
            if stack:
                tem = stack.pop()
                node = tem.right

    return result


if __name__ == '__main__':
    right_node = TreeNode(3)
    head = TreeNode(1, right=right_node)

    # 二叉树数组实现
    # 二叉树的数组实现是按照满二叉树的编号来排列的，如果一个二叉树中的某个节点缺少左子点或右子点，会在对应的编号置空。这样设计是为了能在数组中快速的定位子节点和父节点
    # 那么二叉树数组就满足:
    # 1. 父节点下标为x, 左子节点下标就为2x+1, 右子节点下标就为2x+2
    # 2. 左子节点下标为x, 右子节点下标就为x+1, 那父节点的下标就是(x-1)/2,
    # 3. 右子节点下标为x, 左子节点下标就为x-1, 那父节点的下标就是(x-2)/2
    # 我们会发现，如果一个二叉树是非常稀疏的，也就是树的深度很深，但总节点树其实不多但情况，数组就会有很多空间浪费。所以数组实现最适合二叉堆实现。
    tree_array = [1, None, 3]

    # BFS和DFS
    head.left = TreeNode(2)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    print(dfs(head), dfs(head, 'middle'), dfs(head, 'end'), bfs(head))
    print(stack_dfs(head), stack_dfs(head, 'middle'), stack_dfs(head, 'end'))

