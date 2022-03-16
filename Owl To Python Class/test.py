from chess.svg import piece
from owlready2 import *
from owl_object import *

ONTOLOGY = "file://Chess_Ontology.owl"

def get_all_classes(ontology_path):
    onto = get_ontology(ontology_path).load()

    onto_classes = list(onto.classes())
    classes = []
    for iri in onto_classes:
        iri = str(iri)
        classes.append(iri)
    return classes

def get_all_individuals(ontology_path):
    onto = get_ontology(ontology_path).load()

    onto_ind = list(onto.individuals())
    individuals = []
    for iri in onto_ind:
        iri = str(iri)
        individuals.append(iri)
    return individuals

def generate_all_classes(graph, ontology_path):
    classes = get_all_classes(ontology_path)
    for iri in classes:
        L = iri.split('.')
        name = L[-1]
        graph.add_new_classe(iri, name)

def generate_all_individuals(graph, ontology_path):
    individuals = get_all_individuals(ontology_path)
    for iri in individuals:
        L = iri.split('.')
        name = L[-1]
        graph.add_new_individual(iri, name)

def generate_all_subclass_properties(graph, ontology_path):
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

def generate_triple_list(ontology_path):
    liste_triple = []

    # this request generate all pairs of iri (subject, object) where subject is a subclass of object
    subclasses_pairs = list(default_world.sparql("""
                   SELECT ?subject ?object
    	                WHERE { ?subject rdfs:subClassOf ?object }
            """))

    for (sub_iri, obj_iri) in subclasses_pairs:
        sub_iri = str(sub_iri)
        obj_iri = str(obj_iri)
        liste_triple.append((sub_iri, "SUBCLASSOF", obj_iri))

    return liste_triple

def main():

    chess = graph(name="chess")

    generate_all_classes(chess, ONTOLOGY)
    generate_all_individuals(chess, ONTOLOGY)
    generate_all_subclass_properties(chess, ONTOLOGY)

    # TRY TO PRINT ALL GRAPH INFO
    #chess.print_all()

    #print("====================================================================")
    #print("====================================================================")

    # TRY TO PRINT PIECES SUBCLASSES
    #pieces_iri = "Chess_Ontology.Pieces"
    #pieces_classe = chess.get_classes()[pieces_iri]

    #pieces_classe.print_all()
    
    triple_list = generate_triple_list(ONTOLOGY)

    for t in triple_list:
        print(t)


if __name__ == '__main__':
    main()
