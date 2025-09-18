#This file is to implement and mess around with quick find algorithm
#This should just be missing the global "id" list declaration

id = []
def union_find(p, q, n, id):
    if id[p] == id[q]:
        return
    
    idq = id[q]
    idp = id[p]
    for i in range (n):
        if id[i] == idp:
            id[i] = idq
    return id
    
def find(id, p):
    return id[p]