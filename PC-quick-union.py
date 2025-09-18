#this file is to implement path compression for quick union
id = []
def path_compression(node):
    if id[node] == node:
        return node
    id[node] = path_compression(id[node])
    return id[node]