from owlready2 import *
from OwlToPythonClass.owl_object import *

ONTOLOGY_NAME = "Chess_Ontology"
ONTOLOGY = f"file://resource/{ONTOLOGY_NAME}.owl"


def get_all_classes():
    onto_classes = list(default_world.classes())
    classes = []
    for iri in onto_classes:
        iri = str(iri)
        classes.append(iri)
    return classes


def get_all_individuals():
    onto_ind = list(default_world.individuals())
    individuals = []
    for iri in onto_ind:
        iri = str(iri)
        individuals.append(iri)
    return individuals


def generate_all_classes(graph):
    classes = get_all_classes()
    for iri in classes:
        L = iri.split('.')
        name = L[-1]
        cla = classe(iri, name)
        graph.add_classe(cla)


def generate_all_individuals(graph):
    # this request generate all pairs of iri (ind, cla) where ind is an individual of the class cla
    individuals_pairs = list(default_world.sparql("""
                   SELECT ?individual ?class
    	                WHERE { 
    	                ?individual rdf:type owl:NamedIndividual .
                        ?class rdf:type owl:Class .
    	                ?individual rdf:type ?class }
            """))
    classes = graph.get_classes()

    for (ind_iri, cla_iri) in individuals_pairs:
        cla_iri = str(cla_iri)
        cla = classes[cla_iri]

        ind_iri = str(ind_iri)
        L = ind_iri.split('.')
        name = L[-1]
        ind = individual(ind_iri, name, cla)

        cla.add_individual(ind)
        graph.add_individual(ind)


def generate_all_subclass_properties(graph):
    # this request generate all pairs of iri (subject, object) where subject is a subclass of object
    subclasses_pairs = list(default_world.sparql("""
                   SELECT ?subject ?object
    	                WHERE { ?subject rdfs:subClassOf ?object }
            """))

    classes = graph.get_classes()
    for (sub_iri, obj_iri) in subclasses_pairs:
        sub_iri = str(sub_iri)
        obj_iri = str(obj_iri)
        sub_classe = classes[sub_iri]
        obj_classe = classes[obj_iri]
        obj_classe.add_subclass(sub_classe)


def main():
    chess_graph = graph(name="chess")

    get_ontology(ONTOLOGY).load()

    generate_all_classes(chess_graph)
    generate_all_individuals(chess_graph)
    generate_all_subclass_properties(chess_graph)

    #-# TRY TO PRINT PIECES SUBCLASSES

    # print all graph info command :
    # chess_graph.print_all()

    classes = chess_graph.get_classes()
    individuals = chess_graph.get_individuals()

    pieces_iri = "Chess_Ontology.Pieces"
    cla = classes[pieces_iri]
    cla.print_all()

    rooks_iri = "Chess_Ontology.Rooks"
    cla = classes[rooks_iri]
    cla.print_all()

    R1_iri = "Chess_Ontology.R1"
    ind = individuals[R1_iri]
    ind.print_all()




if __name__ == '__main__':
    main()
