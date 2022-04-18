
import csv
import networkx as nx
import networkx.algorithms.community as nxcom
import matplotlib.pyplot as plt
import community as com

distinct=set()
distinct_target=set()
g = nx.Graph()
l = []
#count=0
f = open('fileg.csv')
csv_f = csv.reader(f)
for row in csv_f:
    if((len(distinct)<5000)):
        distinct.add(row[0])
        distinct.add(row[1])
        #distinct_target.add(row[1])
    if(row[0] in distinct):
        """ if (count==50):
            print(count)
        count=count+1 """
        l.append((row[0],row[1]))
g.add_edges_from(l)

print(nx.info(g))

print(nx.info(g))




print("*********")
print("Is it a Directed Graph-True or False :",nx.is_directed(g))
print("*********")
print("Is it a Weighted Graph-True or False :",nx.is_weighted(g))
print("*********")
print("Edge Density of the network :",nx.density(g))
print("*********")
print("Average clustering coefficient of the network is:",nx.average_clustering(g))
print("*********")
print("The total Connected components in the network is:")
print([len(c) for c in sorted(nx.connected_components(g), key=len, reverse=True)])
print("*********")
print("Diameter of the network is:",nx.diameter(G))
print("*********")
print("The average path length is equal to ",nx.average_shortest_path_length(g))
print("*********")
print("Detecting Communties in the Network :")

p = com.best_partition(g)

values = [p.get(node) for node in G.nodes()]

communities = sorted(nxcom.greedy_modularity_communities(g), key=len, reverse=True)
print(f" {len(communities)} communities.")
print("Number of communities",len(values))
nx.draw_spring(
    g, cmap=plt.get_cmap(), node_color=values, node_size=3, with_labels=False
)
plt.show()
plt.savefig("jan.png")



