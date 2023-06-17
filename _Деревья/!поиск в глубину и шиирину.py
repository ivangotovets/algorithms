graph_2 = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    6: [8, 9],
}


# Поиск в глубину Depth First Search - DFS - Preorder
def dfs_1(graph, head):
    visited = set()
    if head in visited:
        return
    print(f'{head} ', end='')
    visited.add(head)
    sub_trees = graph.get(head, None)
    if sub_trees is not None:
        for node in sub_trees:
            dfs_1(graph, node)


# dfs_1(graph_2, 1)


# Поиск в глубину Depth First Search - DFS - Inorder - Only binary trees
def dfs_2(graph, head):
    children = graph.get(head)
    if children is None:
        print(f'{head} ', end=' ')
    else:
        dfs_2(graph, children[0])
        print(f'{head} ', end=' ')
        dfs_2(graph, children[1])


# dfs_2(graph_2, 1)


# Поиск в глубину Depth First Search - DFS - Postorder - Only binary trees
def dfs_3(graph, head):
    children = graph.get(head)
    if children is None:
        print(f'{head} ', end=' ')
    else:
        dfs_3(graph, children[1])
        dfs_3(graph, children[0])
        print(f'{head} ', end=' ')


# dfs_3(graph_2, 1)


# Поиск в ширину - Breadth First Search - BFS
def bfs(graph, start):
    visited = {start}
    result = [start]
    queue = [start]
    while queue:
        head = queue.pop(0)
        sub_trees = graph.get(head, None)
        if sub_trees is not None:
            for child in sub_trees:
                if child not in visited:
                    visited.add(child)
                    result.append(child)
                    queue.append(child)
    return result


print(bfs(graph_2, 1))


# from queue import Queue
#
# def breadth_first_search(graph: dict, start: str) -> list[str]:
#     explored = {start}
#     result = [start]
#     queue: Queue = Queue()
#     queue.put(start)
#     while not queue.empty():
#         v = queue.get()
#         for w in graph[v]:
#             if w not in explored:
#                 explored.add(w)
#                 result.append(w)
#                 queue.put(w)
#     return result
