"""
反转链表
"""


class Node:
    def __init__(self, next=None, val=None) -> None:
        self.next = next
        self.val = val


def print_nodes(node: Node):
    print(node.val, end="")
    if node.next:
        print("->", end="")
        print_nodes(node.next)
    else:
        # 最后结束的时候, 加个换行
        print()


def reversed_node(node: Node):
    cur_node = node
    next_node = cur_node.next
    # 预先把第一个节点的 next 置空
    cur_node.next = None

    # 如果有当前节点, 和它的下一个节点, 需要反转
    while cur_node and next_node:
        # print(cur_node.val)
        # 预先保存
        third_node = next_node.next
        # 反转
        next_node.next = cur_node
        # 更新状态, 就是移动一位
        cur_node = next_node
        next_node = third_node

    return cur_node


if __name__ == "__main__":
    root = Node(val=1)
    cur = root
    for i in range(2, 6):
        new_node = Node(val=i)
        cur.next = new_node
        cur = new_node
    print_nodes(root)
    new_root = reversed_node(root)
    print_nodes(new_root)
