import itertools

def max_flow(nr_dict, pizzas):
    # for pizza in pizzas:

    comb_len2_list = []
    comb_len2 = itertools.combinations(list(range(len(pizzas))), 2)
    for comb in comb_len2:
        comb_len2_list.append(comb)

    comb_len3 = itertools.combinations(list(range(len(pizzas))), 3)
    comb_len3_list = []
    for comb in comb_len3:
        comb_len3_list.append(comb)
    
    comb_len4_list = []
    comb_len4 = itertools.combinations(list(range(len(pizzas))), 4)
    for comb in comb_len4:
        comb_len4_list.append(comb)
    size_matrix = 1 + len(pizzas) + len(comb_len2_list) + len(comb_len3_list) + len(comb_len4_list) + len(nr_dict) - 1 + 1
   
    flow_graph = []
    for i in range(size_matrix):
        flow_graph.append([0]*size_matrix)

    # print(flow_graph)
    # from the sink to the pizza's
    for i in range(len(pizzas)):
        flow_graph[0][i+1] = 1

    # print(flow_graph)
    # from the pizzas to the combinations
    # and also at the same time to the groups
    # with comb len 2
    for index, comb in enumerate(comb_len2_list):
        # from pizza to comb
        for pizza in comb:
            flow_graph[pizza + 1][index + 1 + len(pizzas)] = 1
        # from comb to group
        for 

    # with comb len 3
    for index, comb in enumerate(comb_len3_list):
        for pizza in comb:
            flow_graph[pizza + 1][index + 1 + len(pizzas) + len(comb_len2_list)] = 1
    
    # with comb len 4
    for index, comb in enumerate(comb_len4_list):
        for pizza in comb:
            flow_graph[pizza + 1][index + 1 + len(pizzas) + len(comb_len2_list) + len(comb_len3_list)] = 1
    
    # 

if __name__ == "__main__":
    nr_dict = {'pizzas': 5, 't2': 1, 't3': 2, 't4': 1}
    pizzas = [(3, {'pepper', 'olive', 'onion'}), (3, {'mushroom', 'basil', 'tomato'}), (3, {'mushroom', 'chicken', 'pepper'}), (3, {'tomato', 'mushroom', 'basil'}), (2, {'chicken', 'basil'})]
    max_flow(nr_dict, pizzas)


# Python program for implementation of Ford Fulkerson algorithm 
   
# from collections import defaultdict 
   
# #This class represents a directed graph using adjacency matrix representation 
# class Graph: 
   
#     def __init__(self,graph): 
#         self.graph = graph # residual graph 
#         self. ROW = len(graph) 
#         #self.COL = len(gr[0]) 
          
   
#     '''Returns true if there is a path from source 's' to sink 't' in 
#     residual graph. Also fills parent[] to store the path '''
#     def BFS(self,s, t, parent): 
  
#         # Mark all the vertices as not visited 
#         visited =[False]*(self.ROW) 
          
#         # Create a queue for BFS 
#         queue=[] 
          
#         # Mark the source node as visited and enqueue it 
#         queue.append(s) 
#         visited[s] = True
           
#          # Standard BFS Loop 
#         while queue: 
  
#             #Dequeue a vertex from queue and print it 
#             u = queue.pop(0) 
          
#             # Get all adjacent vertices of the dequeued vertex u 
#             # If a adjacent has not been visited, then mark it 
#             # visited and enqueue it 
#             for ind, val in enumerate(self.graph[u]): 
#                 if visited[ind] == False and val > 0 : 
#                     queue.append(ind) 
#                     visited[ind] = True
#                     parent[ind] = u 
  
#         # If we reached sink in BFS starting from source, then return 
#         # true, else false 
#         return True if visited[t] else False
              
      
#     # Returns tne maximum flow from s to t in the given graph 
#     def FordFulkerson(self, source, sink): 
  
#         # This array is filled by BFS and to store path 
#         parent = [-1]*(self.ROW) 
  
#         max_flow = 0 # There is no flow initially 
  
#         # Augment the flow while there is path from source to sink 
#         while self.BFS(source, sink, parent) : 
  
#             # Find minimum residual capacity of the edges along the 
#             # path filled by BFS. Or we can say find the maximum flow 
#             # through the path found. 
#             path_flow = float("Inf") 
#             s = sink 
#             while(s !=  source): 
#                 path_flow = min (path_flow, self.graph[parent[s]][s]) 
#                 s = parent[s] 
  
#             # Add path flow to overall flow 
#             max_flow +=  path_flow 
  
#             # update residual capacities of the edges and reverse edges 
#             # along the path 
#             v = sink 
#             while(v !=  source): 
#                 u = parent[v] 
#                 self.graph[u][v] -= path_flow 
#                 self.graph[v][u] += path_flow 
#                 v = parent[v] 
  
#         return max_flow 
  
   
# # Create a graph given in the above diagram 
  
# graph = [[0, 16, 13, 0, 0, 0], 
#         [0, 0, 10, 12, 0, 0], 
#         [0, 4, 0, 0, 14, 0], 
#         [0, 0, 9, 0, 0, 20], 
#         [0, 0, 0, 7, 0, 4], 
#         [0, 0, 0, 0, 0, 0]] 
  
# g = Graph(graph) 
  
# source = 0; sink = 5
   
# print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink)) 
  
# #This code is contributed by Neelam Yadav 