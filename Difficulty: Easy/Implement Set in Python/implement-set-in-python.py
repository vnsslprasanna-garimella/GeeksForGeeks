def insert(s, element):
    s.add(element)

def remove_from_set(s, element):
    s.discard(element)   # safe removal (no error if element not present)

def sum_set(s):
    return sum(s)