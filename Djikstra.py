import heapq

def dijkstra(graph, start_node, node_list):
    short_dist = {}
    pq = []
    heapq.heappush(pq, (0, start_node))
    #Initialize dictionary with infinity for all nodes
    for i in range(len(node_list)):
        short_dist[node_list[i]] = float('inf')
    #Distance from start node to itself is 0
    short_dist[start_node] = 0

    sum_dist = 0;
    while len(pq)>0:
        current = heapq.heappop(pq)[1]
        for next_node in graph[current]:
            new_node = next_node[0]
            #distance between current node and next node
            new_weight = next_node[1]
            if short_dist[current] + new_weight < short_dist[new_node]:
                short_dist[new_node] = short_dist[current] + new_weight
                heapq.heappush(pq, (short_dist[new_node], new_node))
    
    #prepare list containing distances and target nodes
    shortest_pathway = []
    for node in node_list:
        shortest_pathway.append((node, short_dist[node])) 

    return shortest_pathway


#test adjacency list
graph = {
    'A':{'B': 4, 'C': 2},
    'B':{'A': 4, 'C': 1, 'D': 5},
    'C':{'A': 2, 'B': 1, 'D': 8},
    'D':{'B': 5, 'C': 8}
}

print(dijkstra(graph, 'A', ['A', 'B', 'C', 'D']))

#suppose start node = A
#A -> B -> C -> D
#A -> C -> B -> D
#A -> B -> D -> C
#A -> C -> D -> B

#AB: 4
#ACB: 3
#ACDB: 15

#AC: 2
#ABC: 6
#ABDC: 17

#ABD: 9
#ACD: 10