from collections import defaultdict

def find_route_and_tax(N, cities):
    graph = defaultdict(list)

    for _ in range(N - 1):
        city1, city2, goods, tax = input().split()
        goods, tax = int(goods), int(tax)
        graph[city1].append((city2, goods, tax))
        graph[city2].append((city1, goods, tax))

    visited = set()
    route = []
    total_tax = 0

    def dfs(city):
        nonlocal total_tax

        visited.add(city)
        neighbors = sorted(graph[city], key=lambda x: (-x[1], x[2], x[0]))

        for neighbor in neighbors:
            next_city, goods, tax = neighbor
            if next_city not in visited:
                total_tax += tax
                route.append(next_city)
                dfs(next_city)
                route.append(city)

    start_city = list(graph.keys())[0]
    route.append(start_city)
    dfs(start_city)

    route_map = "-".join(route)
    return route_map, total_tax

def main():
    N = int(input())
    route_map, total_tax = find_route_and_tax(N, [])

    print(route_map)
    print(total_tax)

if __name__ == "__main__":
    main()
