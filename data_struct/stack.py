import unittest


class Stack:
    """将列表的最后一个元素当作栈的顶端"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class TestStack(unittest.TestCase):
    def test_stack(self):
        """这个一定是哪里抄来的, 因为我看的书上正好是这个例子, 哪些参数都是一样的"""
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(4)
        s.push("dog")
        self.assertEqual(s.peek(), "dog")
        s.push(True)
        self.assertEqual(s.size(), 3)
        self.assertFalse(s.is_empty())
        s.push(8.4)
        self.assertEqual(s.pop(), 8.4)
        self.assertEqual(s.pop(), True)
        self.assertEqual(s.size(), 2)
