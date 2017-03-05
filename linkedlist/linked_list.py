class Node(object):
    def __init__(self, value):
        self.next_node = None
        self.value = value
        

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, elem):
        if self.head is None:
            self.head = Node(elem)
            self.tail = self.head
        else:
            self.tail.next_node = Node(elem)
            self.tail = self.tail.next_node

    def insert(self, elem):
        new_node = Node(elem)
        new_node.next_node = self.head
        self.head = new_node

    def get_size(self):
        l = 0
        node = self.head
        while node is not None:
            l += 1
            node = node.next_node
        return l

    def find_element(self, elem):
        node = self.head
        while node is not None:
            if node.value == elem:
                return node
            node = node.next_node
        return ValueError

    def delete_element(self, elem):
        node = self.head
        found = False
        prev_node = None
        while node is not None and found is False:
            if node.value == elem:
                found = True
            else:
                prev_node = node
                node = node.next_node
        if node is None:
            raise ValueError
        if prev_node is None:
            self.head = node.next_node
        else:
            previous.next_node = node.next_node

    def __str__(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next_node
        return ", ".join(map(str, result))

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev

def has_loop(node):
    if node is None:
        return False

    slow = fast = node

    while True:
        slow = slow.next_node
        if fast.next_node is not None:
            fast = fast.next_node.next_node
        else:
            return False
        if slow is None or fast is None:
            return False
        if slow == fast:
            return True
