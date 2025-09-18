#this code is to implement and mess around with quick union

def quick_union(p, q, id):
    idp = find(id, p)
    idq = find(id, q)

    if idp == idq:
        return
    
    id[idp] = idq

def find(id, p):
    while id[p] != p:
        p = id[p]
    return p