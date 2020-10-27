import sys 
sys.setrecursionlimit(10**6) 

class Node:
    def __init__(self, data):
        self.data = data 
        self.childrens = []
        self.parent = None 
        self.no_of_childrens = 0 


def get_subordinates(tree,v):
    if tree[v].childrens: 
        ans = 0 
        for i in tree[v].childrens:
            ans += get_subordinates(tree, i)
        tree[v].no_of_childrens = ans + len(tree[v].childrens)
        return tree[v].no_of_childrens
    else:
        return 0 

def solve():
    n = int(input())
    tree = dict()
    for i in range(1,n+1):
        tree[i] = Node(i)
    p = list(map(int,input().split()))
    c = 2 
    for i in p:
        tree[i].childrens.append(c)
        tree[c].parent = i 
        c += 1 
    get_subordinates(tree, 1)
    
    for i in range(1,n+1):
        print(tree[i].no_of_childrens, end = " ")


if __name__ == '__main__':
    solve()