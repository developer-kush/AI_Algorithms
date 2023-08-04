import sys, time

sys.stdin = open('_in.txt','r+')
sys.stdout = open('_out.txt','w+')

start_time = time.perf_counter()

# ---------------------------------------------------------------------------------



"""
# ALGORITHM 

1. Key function, is f(n) = g(n) + h(n)
2. Assuming heuristic as Euclidean distance
3. Assuming cost as Euclidean distance
"""

from heapq import heappush, heappop, heapify

def A_Search(n, m, cities, connections, src, dest):

    def getDist(cityA, cityB):
        return ((cities[cityA][0]- cities[cityB][0])**2 + (cities[cityA][1]- cities[cityB][1])**2)**0.5
    
    def getHeuristic(cityA, cityB):
        return ((cities[cityA][0]- cities[cityB][0])**2 + (cities[cityA][1]- cities[cityB][1])**2)**0.5
    
    def getCost(cityA, cityB):
        return getDist(cityA, cityB)+getHeuristic(cityB, dest)
    
    hp = [[0, 0, src]]
    res = float('inf')
    while hp:
        cost, actual, city = heappop(hp)
        if cost>res: continue
        if city == dest:
            res = min(res, actual)
            continue
        for neighbor in connections[city]:
            dist = cost + getCost(city, neighbor)
            if dist<res: heappush(hp, [dist, actual+getDist(city, neighbor), neighbor])
    
    if res == float('inf'): return -1
    return res


n, m, = list(map(int, input().split()))
cities = {}
for city in range(n):
    x, y = list(map(int, input().split()))
    cities[city] = x, y
connections = {}
for _ in range(m):
    cityA, cityB = list(map(int, input().split()))
    if cityA not in connections: connections[cityA] = []
    if cityB not in connections: connections[cityB] = []
    connections[cityA].append(cityB)
    connections[cityB].append(cityA)

# PRETTY OUTPUT
print("CITY MAP")
map = [['.' for _ in range(max(x[1] for x in cities.values())+1)] for _ in range(max(x[0] for x in cities.values())+1)]
for city, pos in cities.items(): map[pos[0]][pos[1]] = city
for row in map: print(*row)
print("\nDISTANCES")
for dest in range(n):
    print(dest,":",format(A_Search(n, m, cities, connections, 0, dest),'.5f'))



# ---------------------------------------------------------------------------------
print(f"{'-'*20} {time.perf_counter()-start_time * 1000}ms {'-'*20}")