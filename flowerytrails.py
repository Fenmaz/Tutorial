from queue import PriorityQueue

def inp():
    first_line = input().split(" ")
    num_points, num_trails = int(first_line[0]), int(first_line[1])
    adj_lst = {i: set() for i in range(num_points)}
    trail_len = {}
    trail_len_duplicate_count = {}
    for i in range(num_trails):
        trail = input().split(" ")
        node1, node2, length = int(trail[0]), int(trail[1]), int(trail[2])
        if node1 != node2:
            adj_lst[node1].add(node2)
            adj_lst[node2].add(node1)
            key = frozenset((node1, node2))
            if key in trail_len and length >= trail_len[key]:
                trail_len_duplicate_count[key] += 1 if length == trail_len[key] else 0
            else:
                trail_len[key] = length
                trail_len_duplicate_count[key] = 1
    return num_points, adj_lst, trail_len, trail_len_duplicate_count


def main():
    num_points, adj_lst, trail_len, trail_len_duplicate_count = inp()
    shortest_path = sum(trail_len.values())
    flower_path = set(trail_len.keys())
    queue = Queue()
    visited = {node: False for node in nodes}
    prev = {}
    queue.add((0, 0))
    visited[0] = True

    while not queue.empty():
        current_dist, current_node = queue.get()
        if current_dist > shortest_path:
            break
        if current_node == num_points - 1:
            shortest_path = current_dist
        for neighbor in adj_lst[current_node]:
            if not visited[neighbor]:
                queue.put((
    # print(flower_path)
    return sum(trail_len[path] * trail_len_duplicate_count[path] for path in flower_path) * 2

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main"))

