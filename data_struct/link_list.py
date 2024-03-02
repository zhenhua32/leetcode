import unittest


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


# 未经检查的代码
class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """插入节点是在头部插入"""
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        """在尾部添加节点"""
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        temp = Node(item)
        current.set_next(temp)

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.get_data() == item:
                return count
            current = current.get_next()
            count += 1
        return -1

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.get_next()
            count += 1
        temp = Node(item)
        if previous is None:
            temp.set_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def pop(self, pos=None):
        if pos is None:
            current = self.head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            if previous is None:
                self.head = None
            else:
                previous.set_next(None)
            return current.get_data()
        else:
            current = self.head
            previous = None
            count = 0
            while count < pos:
                previous = current
                current = current.get_next()
                count += 1
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            return current.get_data()


class TestUnorderedList(unittest.TestCase):
    def test_unordered_list(self):
        my_list = UnorderedList()
        self.assertTrue(my_list.is_empty())
        my_list.add(31)
        my_list.add(77)
        my_list.add(17)
        my_list.add(93)
        my_list.add(26)
        my_list.add(54)
        self.assertEqual(my_list.size(), 6)
        self.assertTrue(my_list.search(93))
        my_list.remove(54)
        self.assertEqual(my_list.size(), 5)
        my_list.append(100)
        self.assertEqual(my_list.size(), 6)
        self.assertEqual(my_list.index(93), 1)
        my_list.insert(1, 200)
        self.assertEqual(my_list.size(), 7)
        self.assertEqual(my_list.pop(), 100)
        self.assertEqual(my_list.pop(1), 200)
        self.assertEqual(my_list.size(), 5)
        self.assertEqual(my_list.pop(0), 26)
        self.assertEqual(my_list.size(), 4)
        self.assertEqual(my_list.pop(0), 93)
        self.assertEqual(my_list.size(), 3)
        self.assertEqual(my_list.pop(0), 17)
        self.assertEqual(my_list.size(), 2)
        self.assertEqual(my_list.pop(0), 77)
        self.assertEqual(my_list.size(), 1)
        self.assertEqual(my_list.pop(0), 31)
        self.assertEqual(my_list.size(), 0)
        self.assertTrue(my_list.is_empty())
