import unittest


class Deque:
    """使用列表实现, 列表的最后一个元素是前端, 第一个元素是后端"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        """所以, 这里添加到前端, 就是添加到列表的最后一个元素"""
        self.items.append(item)

    def add_rear(self, item):
        """这里是添加到后端"""
        self.items.insert(0, item)

    def remove_front(self):
        """移除前端的第一个元素"""
        return self.items.pop()

    def remove_rear(self):
        """移除后端的第一个元素"""
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class TestDeque(unittest.TestCase):
    def test_deque(self):
        d = Deque()
        self.assertTrue(d.is_empty())
        d.add_rear(4)
        d.add_rear("dog")
        self.assertEqual(d.size(), 2)
        self.assertFalse(d.is_empty())
        d.add_front(True)
        # 当前的结构是 ["dog", 4, True]
        self.assertEqual(d.remove_rear(), "dog")
        self.assertEqual(d.remove_front(), True)
        self.assertEqual(d.size(), 1)
        self.assertEqual(d.remove_rear(), 4)
        self.assertTrue(d.is_empty())
