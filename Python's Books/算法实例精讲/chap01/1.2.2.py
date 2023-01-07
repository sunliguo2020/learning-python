# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-07 7:59
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class singlelink:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return

    def isempty(self):
        return self.length == 0

    def add_node(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            self.tail = item
        self.length += 1
        return

    def insert_node(self, index, data):
        if self.isempty():
            print('this link is empty')
            return
        if index < 0 or index >= self.length:
            print("error:out of index")
            return
        item = Node(data)
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def delete_node_byid(self, item_id):
        id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if id == item_id:
                if previous_node is not None:
                    previous_node.netx = current_node
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            id = id + 1
        self.length -= 1
        return

    def find_node(self, value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def print_link(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        return


print(Node(1))
print(Node(1).__dict__)
