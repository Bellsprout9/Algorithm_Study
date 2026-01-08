# 트리와 쿼리
from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R, Q = map(int, input().split())

graph = defaultdict(list)
nodes = set()
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    nodes.add(u)
    nodes.add(v)

parents = {v:0 for v in nodes}
child = {v:[] for v in nodes}

def makeTree(currentNode, parent):
    parents[currentNode] = parent
    for nextNode in graph[currentNode]:
        if nextNode != parent:
            child[currentNode].append(nextNode)
            makeTree(nextNode, currentNode)

size = {v:0 for v in nodes}

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for nextNode in child[currentNode]:
        countSubtreeNodes(nextNode)
        size[currentNode] += size[nextNode]

makeTree(R, -1)
countSubtreeNodes(R)

for i in range(Q):
    u = int(input())
    print(size[u])