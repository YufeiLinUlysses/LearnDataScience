# numbers
a = 3
b = 3.4

# list
m = [1, 2, "3", 4]

# tuples, not writable, only readable
c = (a, b)
d = (a, b, c)

# set, the same definition of set in math
s = set()
s.add(1)
print(s)
s.add(1)
print(s)
k = set()
k.add(2)
k.add(1)
print(k)
print(s.union(k))
print(s.intersection(k))
print(s-k)

# dictionary
d = {"key": "value"}
print(d["key"])
for key, value in d.items():
    print(key)
    print(value)
