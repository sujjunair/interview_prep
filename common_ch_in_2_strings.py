a = "juice"
b = "sujit"
result = []
for ch in a:
    if ch in b:
        result.append(ch)
print "".join(result)
