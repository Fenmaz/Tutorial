from queue import Queue


def inp():
    first_line = input().split(" ")
    num_points, num_trails = int(first_line[0]), int(first_line[1])
    adj_lst = {i: set() for i in range(num_points)}
    trail_len = {}
    for i in range(num_trails):
        trail = input().split(" ")
        node1, node2, length = int(trail[0]), int(trail[1]), int(trail[2])
        if node1 != node2:
            adj_lst[node1].add(node2)
            adj_lst[node2].add(node1)
            key = frozenset((node1, node2))
            trail_len[key] = min(length, trail_len[key]) if key in trail_len else length
    return num_points, adj_lst, trail_len


def main():
    num_points, adj_lst, trail_len = inp()
    # print(adj_lst)
    # print(trail_len)
    shortest_path = sum(trail_len.values())
    flower_path = set(trail_len.keys())

    def dfs_recur(current_node, path):
        nonlocal shortest_path, flower_path
        if current_node == num_points - 1:
            edges = [frozenset((path[i], path[i+1])) for i in range(len(path) - 1)]
            length = sum(trail_len[edge] for edge in edges)
            if length < shortest_path:
                flower_path = set(edges)
                shortest_path = length
            elif length == shortest_path:
                flower_path = flower_path.union(edges)
        for node in adj_lst[current_node]:
            if node not in path:
                dfs_recur(node, path.copy().append(node))

    dfs_recur(0, [0])
    print(flower_path)
    return sum(trail_len[path] for path in flower_path) * 2

if __name__ == '__main__':
    print(main())
