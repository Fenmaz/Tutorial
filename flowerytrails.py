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
            if key not in trail_len or length < trail_len[key]:
                trail_len[key] = length
                trail_len_duplicate_count[key] = 1
            elif length == trail_len.get(key):
                trail_len_duplicate_count[key] += 1

    return num_points, adj_lst, trail_len, trail_len_duplicate_count


def main():
    num_points, adj_lst, trail_len, trail_len_duplicate_count = inp()
    shortest_path = 0
    queue = PriorityQueue()
    dist = {0: 0}
    prev = {0: []}
    queue.put((0, 0))

    while not queue.empty():
        current_dist, current_node = queue.get()
        if shortest_path and current_dist > shortest_path:
            break
        if current_node == num_points - 1:
            shortest_path = current_dist
            continue
        for neighbor in adj_lst[current_node]:
            alt = current_dist + trail_len[frozenset((current_node, neighbor))]
            if neighbor not in dist or alt <= dist[neighbor]:
                queue.put((alt, neighbor))
                prev.setdefault(neighbor, []).append(current_node)
                dist[neighbor] = alt

    stack = [num_points - 1]
    flower_path = set()
    while stack:
        node = stack.pop()
        for neighbor in prev[node]:
            flower_path.add(frozenset((node, neighbor)))
            stack.append(neighbor)
    # print(flower_path)
    return sum(trail_len[path] * trail_len_duplicate_count[path] for path in flower_path) * 2

if __name__ == '__main__':
    # from time import clock
    # start_time = clock()
    print(main())
    # print("Time: {:.4f}".format(clock() - start_time))
