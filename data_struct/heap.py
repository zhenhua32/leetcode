class BinaryHeap:
    """
    这是个最小二叉堆, 也就是根节点的值最小
    """

    def __init__(self):
        """初始化二叉堆"""
        # 第一个元素是占位符, 为了方便后续的计算
        self.heapList = [0]
        # 当前堆的大小
        self.currentSize = 0

    def percUp(self, i):
        """上浮元素, 使其满足堆的性质"""
        while i // 2 > 0:
            # 当前节点的值小于其父节点的值, 则交换两者的值
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        """插入元素到堆中"""
        # 插入元素到堆的末尾
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        # 调整堆, 使其满足堆的性质
        self.percUp(self.currentSize)

    def percDown(self, i):
        """下沉元素, 使其满足堆的性质"""
        while (i * 2) <= self.currentSize:
            # 找到当前节点的两个子节点中的最小值
            mc = self.minChild(i)
            # 如果当前节点的值大于其子节点的值, 则交换两者的值
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """找到当前节点的两个子节点中的最小值"""
        # 如果当前节点的左子节点已经是最后一个节点, 那么当前节点就没有右子节点
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # 如果当前节点的左子节点的值小于右子节点的值, 那么返回左子节点的索引
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                # 否则返回右子节点的索引
                return i * 2 + 1

    def delMin(self):
        """删除堆中的最小元素, 也就是根节点的元素"""
        # 最小元素
        retval = self.heapList[1]
        # 将堆的最后一个元素放到根节点, 然后删除最后一个元素
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # 调整堆, 使其满足堆的性质
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        """构建堆, 使其满足堆的性质"""
        i = len(alist) // 2
        self.currentSize = len(alist)
        # 第一个元素是占位符, 为了方便后续的计算. 添加所有元素
        self.heapList = [0] + alist[:]
        while (i > 0):
            # 使用下沉操作, 使其满足堆的性质
            self.percDown(i)
            i = i - 1
