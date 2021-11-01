from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next_value = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete

        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if not self.head:
            return False
        if self.head.value == value:
            if self.head.next_value:
                self.head = self.head.next_value
            else:
                self.head = None
            return True
        link = self.head.next_value
        prev = self.head
        while link:
            if link.value == value:
                prev.next_value = link.next_value
                return True
            prev = link
            link = link.next_value
        return False

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        link = self.head
        while link:
            if link.value == value:
                return link
            link = link.next_value
        return link

    def append(self, value):
        """
        Add element to linked list
        """
        if not self.head:
            self.head = Node(value)
            return
        link = self.head
        while link.next_value:
            link = link.next_value
        link.next_value = Node(value)
        return


def binary_search(input_list: List[Union[int, float, str]], value: Union[int, float, str]) -> Optional[int]:
    left = 0
    right = len(input_list) - 1
    while left <= right:
        m = (left + right) // 2
        if input_list[m] == value:
            return m
        elif input_list[m] < value:
            left = m + 1
        else:
            right = m - 1
    return None


class BTSNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, node=None):
        self.root = node

    def __getitem__(self, key) -> Optional[BTSNode]:
        """
        find and return requested node
        """
        link = self.root
        if not link:
            return None
        if link.value == key:
            return link
        if link.value > key:
            return BinaryTree(link.left).__getitem__(key)
        else:
            return BinaryTree(link.right).__getitem__(key)

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        if not self.root:
            return None
        if self.root.value > key:
            self.root.left = BinaryTree(self.root.left).__delitem__(key)
        elif self.root.value < key:
            self.root.right = BinaryTree(self.root.right).__delitem__(key)
        else:
            if not self.root.left:
                temp = self.root.right
                self.root = None
                return temp
            elif not self.root.right:
                temp = self.root.left
                self.root = None
                return temp

            temp = self.root.right
            while temp.left:
                temp = temp.left

            self.root.value = temp.value
            self.root.right = BinaryTree(self.root.right).__delitem__(temp.value)
        return self.root

    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        if not self.root:
            self.root = bts_node
        else:
            if self.root.value < bts_node.value:
                self.root.right = BinaryTree(self.root.right).append(bts_node)
            elif self.root.value > bts_node.value:
                self.root.left = BinaryTree(self.root.left).append(bts_node)
        return self.root
