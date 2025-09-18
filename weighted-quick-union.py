#this file is for weighted quick union
#no self references, need to add
def __init__(self, n):
          self.id = list(range(n))
          self.size = [1] * n

def W_quick_union(p, q, id):
    idq = find(id, q)
    idp = find(id, p)

    if idp == idq:
        return
    
    
    for i in range (len(id)):
        size[i] = 1

    if size[idp] >= size[idq]:
        id[idq] = idp
        size[idp] += size[idq]
    
    elif size[idq] > size[idp]:
        id[idp] = idq
        size[idq] += size[idp]

def find(id, p):
    while id[p] != p:
        p = id[p]
    return p
