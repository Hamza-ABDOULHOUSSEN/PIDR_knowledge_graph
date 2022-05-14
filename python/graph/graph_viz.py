import graphviz

from OwlToRdf.conversion_owl_to_rdf import *

ONTOLOGY_NAME = "pizza"
ONTOLOGY = f"file://resource/{ONTOLOGY_NAME}.owl"


def complete_graph_subclasses(G, subclasses):
    for triple in subclasses:
        G.node(triple[2], style="filled", color="skyblue", shape="ellipse")
        G.node(triple[0], style="filled", color="skyblue", shape="ellipse")
        G.edge(triple[2], triple[0], label="Subclass", shape="normal")

def complete_graph_individuals(G, individuals):
    for triple in individuals:
        G.node(triple[2], style="filled", color="skyblue", shape="ellipse")
        G.node(triple[0], style="filled", color="purple", shape="box")
        G.edge(triple[2], triple[0], label="Individual", shape="normal")

def complete_graph_properties(G, properties):
    for triple in properties:
        G.edge(triple[0], triple[2], label=triple[1], shape="normal")

def main():
    # main()
    # load the ontology
    get_ontology(ONTOLOGY).load()

    # create the graph
    G = graphviz.Digraph()

    subclasses = generate_triple_list_subclass()
    individuals = generate_triple_list_individuals()
    properties = generate_triple_list_object_properties()

    subclasses = remove_restriction(subclasses)
    individuals = remove_restriction(individuals)
    properties = remove_restriction(properties)

    complete_graph_subclasses(G, subclasses)
    complete_graph_individuals(G, individuals)
    complete_graph_properties(G, properties)

    G.view()


if __name__ == '__main__':
    main()