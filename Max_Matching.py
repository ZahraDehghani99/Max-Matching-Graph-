import matplotlib.pyplot as plt
import networkx as nx
from networkx import bipartite

def plotGraph(graph, ax, title):

    pos = [(node[1], node[0]) for node in graph.nodes()]
    pos_dict = dict(zip(graph.nodes(), pos))
    nx.draw(graph, pos=pos_dict, ax=ax, with_labels=True)
    ax.set_title(title)
    return

# ---------------Construct the graph---------------

g = nx.Graph() #  Graph() class can be used to represent bipartite graphs.

edges = [
            [(1,0), (0,0)],
            [(1,0), (0,1)],
            [(1,0), (0,2)],
            [(1,1), (0,0)],
            [(1,2), (0,2)],
            [(1,2), (0,5)],
            [(1,3), (0,2)],
            [(1,3), (0,3)],
            [(1,4), (0,3)],
            [(1,5), (0,2)],
            [(1,5), (0,4)],
            # [(1,5), (0,6)],
            [(1,6), (0,1)],
            [(1,6), (0,4)],
            # [(1,6), (0,6)]
            ]  # edges of the input graph


for edge in edges:
    g.add_node(edge[0], bipartite=0)  # bipartite with values 0 or 1 to identify the sets each node belongs to
    g.add_node(edge[1], bipartite=1)


g.add_edges_from(edges)  # Add edges only between nodes of opposite node sets


# ----------Use bipartite.maximum_matching----------
match2 = bipartite.maximum_matching(g)
print(match2)  # The dictionary returned by maximum_matching() includes a mapping for vertices in both vertex sets.
g_match2 = nx.Graph()
for item0, item1 in match2.items():
    g_match2.add_edge(item0, item1)

# -----------------------Plot-----------------------

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(2, 2, 1)
plotGraph(g, ax1, 'Graph')

ax2 = fig.add_subplot(2, 2, 3)
plotGraph(g_match2, ax2, 'bipartite maximum matching')

plt.show() #  show the input graph and maximum matching of input graph
