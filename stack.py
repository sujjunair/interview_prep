class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return ValueError

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return ",".join(map(str, self.items))
'''    
s = Stack()
s.push('s')
s.push('u')
s.push('j')
print s.peek()
print s.pop()
print s.pop()
print s.pop()
'''
