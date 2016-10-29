from stack import Stack

arr = [40,50,11,32,55,68,75]
result = []
s = Stack()
s.push(arr[0])
for nxt in arr[1:]:
    # if next element causes the 
    # stack to pop elements, then
    # record it
    if nxt > s.peek():
        while not s.is_empty() and nxt > s.peek():
            a = s.pop()
            result.append((a, nxt))
        s.push(nxt)
    else:
        s.push(nxt)
# whatever is left over, has no next
while not s.is_empty():
    result.append((s.pop(), -1))
print result
