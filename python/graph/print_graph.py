import spacy
from spacy.lang.en import English
import networkx as nx
import matplotlib.pyplot as plt

from OwlToRdf.conversion_owl_to_rdf import *

ONTOLOGY = "file://resource/pizza_some.owl"
ONTOLOGY_NAME = "pizza_some"

def printGraph(triples):
    G = nx.Graph()

    # initiate dict
    node_shape = {}

    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[2])
        node_shape[triple[0]] = "o"
        node_shape[triple[2]] = "o"
        G.add_edge(triple[0], triple[2])
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    print(G.nodes())
    print(node_shape)

        
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='skyblue', alpha=0.9, arrowstyle='->',
            node_shape=node_shape,
            arrows=True,
            labels={node: node for node in G.nodes()})
            



    plt.axis('off')
    plt.savefig('graph/plots/myplot.png')


def main():
    # main()
    # load the ontology
    get_ontology(ONTOLOGY).load()

    triple_list = generate_triple_list_individuals()

    printGraph(triple_list)

if __name__ == '__main__':
    main()