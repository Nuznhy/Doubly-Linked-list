#!/bin/python3


class Node:

    def __init__(self, data):
        self.data = data  # Storage for data
        self.next = None  # Reference to next item
        self.prev = None  # Reference to previous item


class LinkedList:

    def __init__(self):
        self.head = None  # start of the node
        self.tail = None  # end of the node
        self.len = 0

    def __getitem__(self, key):
        current = self.head
        for i in range(key):
            current = current.next
        return current.data

    class LLIterator:
        def __init__(self, head):
            self.current_node = head

        def __next__(self):
            if self.current_node is None:
                raise StopIteration

            value = self.current_node.data
            self.current_node = self.current_node.next
            return value

    def __iter__(self):
        return self.LLIterator(self.head)

    def size(self):  # return size of the list (number of elements in it)
        return self.len

    def print(self):
        for i in range((self.size())-1, -1, -1):
            print(float("%.1f" % self[i]), end=' ')
        print()
        for i in self:
            print(float("%.1f" % i), end=' ')

    def push(self, data):  # add an item to the end of the list
        new_data = Node(data)
        self.len += 1
        if self.head is None:  # Check if list actually exist
            self.head = new_data  # if not exist, then apply head element to item
            new_data.prev = None  # if head is the first item, then you have not got any next or prev items
            new_data.next = None
            self.tail = new_data  # tale is also head and item
        else:
            self.tail.next = new_data  # if head is not item, then we are injecting new item and apply it to tail
            new_data.prev = self.tail
            self.tail = new_data

    def unshift(self, data):  # add an item to the head of the list
        new_data_unshift = Node(data)
        self.len += 1
        if self.head is None:
            self.head = new_data_unshift  # if not exist, then apply head element to item
            new_data_unshift.prev = None  # if head is the first item, then you have not got any next or prev items
            new_data_unshift.next = None
            self.tail = new_data_unshift  # tale is also head and item
        else:
            self.head.prev = new_data_unshift  # if head is not item then we inject new item and apply it to head
            new_data_unshift.next = self.head
            new_data_unshift.prev = None
            self.head = new_data_unshift

    def pop(self):
        if self.head is None:
            return None
        else:
            self.len -= 1
            if self.head != self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
                return self.tail
            else:
                self.head = self.tail = None
                return self.tail

    def shift(self):
        if self.head is None:
            return None
        else:
            self.len -= 1
            if self.head != self.tail:
                self.head = self.head.next
                self.head.prev = None
                return self.head
            else:
                self.head = self.tail = None
                return self.head

    def insert(self, index, data):
        new_data = Node(data)
        cur = self.head
        if index == 0:
            self.unshift(data)
        elif index >= self.size():
            self.push(data)
        else:
            self.len += 1
            for i in range(index):
                cur = cur.next
            new_data.next = cur
            new_data.prev = cur.prev
            cur.prev.next = new_data
            cur.prev = new_data

    def find(self, v):
        cur = self.head
        while cur.data != v:
            if cur is None:
                return None
            cur = cur.next
        #print(cur)
        return cur

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if (count == index):
                return current.data
            count += 1
            current = current.next
            #print(current.data)
            return current

DoubleLinkedList = LinkedList()

N = int(input())
if N != 0:
    numbers = input().strip().split()
    # print(numbers)
    numbers = [int(n) for n in numbers]
    for i in numbers:
        DoubleLinkedList.push(i)

# print('Insert number of operations: ')
M = int(input())
for i in range(M):
    operation = input().strip().split()
    if operation[0] == 'pop':
        DoubleLinkedList.pop()
        # DoubleLinkedList.print()
    if operation[0] == 'shift':
        DoubleLinkedList.shift()
        # DoubleLinkedList.print()
    if operation[0] == 'print':
        DoubleLinkedList.print()
    if operation[0] == 'size':
        DoubleLinkedList.size()
    if operation[0] == 'push':
        DoubleLinkedList.push(float(operation[1]))
        # DoubleLinkedList.print()
    if operation[0] == 'unshift':
        DoubleLinkedList.unshift(float(operation[1]))
        # DoubleLinkedList.print
    if operation[0] == 'find':
        DoubleLinkedList.find(float(operation[1]))
    if operation[0] == 'get':
        DoubleLinkedList.get(int(operation[1]))
    if operation[0] == 'insert':
        DoubleLinkedList.insert(int(operation[1]), float(operation[2]))

#node1 = Node(1)
#node2 = Node(2)
#node3 = Node(3)
#DoubleLinkedList.push(node1)
#DoubleLinkedList.push(node2)
#DoubleLinkedList.push(node3)
#DoubleLinkedList.reverse()
#DoubleLinkedList.print()
# DoubleLinkedList.find(3.0)
# DoubleLinkedList.find(2)
# DoubleLinkedList.reverse()
DoubleLinkedList.print()

