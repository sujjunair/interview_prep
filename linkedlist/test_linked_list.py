from linked_list import LinkedList

a = LinkedList()
a.add(20)
a.add(43)
a.add(8)
a.add(5)
a.add(34)
a.add(9)

print a
print a.find_element(8).value
a.reverse()
print a
