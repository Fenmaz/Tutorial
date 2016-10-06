def inp():
        first_line = input().split(" ")
        num_points, num_trails = int(first_line[0]) , int(first_line[1])
        adj_lst = [[]  * num_points]
        trail_len = {}
        for i in range(num_trails):
                trail = input().split(" ")
                node1, node2, length = int(trail[0]), int(trail[1]), int(trail[2])
                adj_lst[node1].append(node2)
                adj_lst[node2].append(node2)
                trail_len[node1, node2], trail_len[node2, node1] = length
        return num_points, adj_lst, trail_len


def main():
        num_points, adj_lst, trail_len = inp()
        shortest_path = 0
        stack = [0]
        path = []
        while stack != []:
                cur_node = stack.pop()
                path.append(cur_node)
                for node in adj_lst[cur_node]:
                        if node not in path:
                                stack.append[node]

