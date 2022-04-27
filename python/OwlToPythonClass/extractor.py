from owlready2 import *
import string
from OwlToPythonClass.owl_object import *


ONTOLOGY = "file://resource/pizza_some.owl"
ONTOLOGY_NAME = "pizza_some"
PRINT_INFO = 1         # 0 for no and 1 for yes
CREATE_OUTPUT = 1         # 0 for no and 1 for yes

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
        graph.add_new_classe(iri, name)

def generate_all_individuals(graph):
    individuals = get_all_individuals()
    for iri in individuals:
        L = iri.split('.')
        name = L[-1]
        graph.add_new_individual(iri, name)

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

def generate_triple_list_subclass():
    liste_triple = []

    # this request generate all pairs of iri (subject, object) where subject is a subclass of object
    subclasses_pairs = list(default_world.sparql("""
                   SELECT ?subject ?object
    	                WHERE { ?subject rdfs:subClassOf ?object }
            """))

    for (sub_iri, obj_iri) in subclasses_pairs:
        sub_iri = str(sub_iri)
        obj_iri = str(obj_iri)
        liste_triple.append((sub_iri, "subClassOf", obj_iri))

    return liste_triple

def generate_triple_list_individuals():
    liste_triple = []

    # this request generate all pairs of iri (ind, cla) where ind is an individual of the class cla
    subclasses_pairs = list(default_world.sparql("""
                   SELECT ?individual ?class
    	                WHERE { 
    	                ?individual rdf:type owl:NamedIndividual .
                        ?class rdf:type owl:Class .
    	                ?individual rdf:type ?class }
            """))

    for (ind_iri, cla_iri) in subclasses_pairs:
        ind_iri = str(ind_iri)
        cla_iri = str(cla_iri)
        liste_triple.append((ind_iri, "individualOf", cla_iri))

    return liste_triple

def generate_triple_list_object_properties():
    liste_triple = []

    # this request generate all pairs of iri (prop, dom) where dom is the domain of the property prop
    domain_list = list(default_world.sparql("""
                       SELECT ?prop ?dom
        	                WHERE { ?prop rdfs:domain ?dom }
                """))

    # this request generate all pairs of iri (prop, ran) where ran is the range of the property prop
    range_list = list(default_world.sparql("""
                       SELECT ?prop ?ran
        	                WHERE { ?prop rdfs:range ?ran }
                """))

    # creation of the dictionary
    domain_dic = {}
    range_dic = {}

    for (prop_iri, obj_iri) in domain_list:
        prop_iri = str(prop_iri)
        obj_iri = str(obj_iri)
        if prop_iri in domain_dic.keys():
            domain_dic[prop_iri].append(obj_iri)
        else:
            domain_dic[prop_iri] = [obj_iri]

    for (prop_iri, obj_iri) in range_list:
        prop_iri = str(prop_iri)
        obj_iri = str(obj_iri)
        if prop_iri in range_dic.keys():
            range_dic[prop_iri].append(obj_iri)
        else:
            range_dic[prop_iri] = [obj_iri]

    for prop in domain_dic.keys():
        for dom in domain_dic[prop]:
            for ran in range_dic[prop]:
                liste_triple.append((dom, prop, ran))

    return liste_triple

def generate_triple_list_equivalent():
    liste_triple = []

    # this request generate all pairs of iri (prop, dom) where dom is the domain of the property prop
    equivalent_list = list(default_world.sparql("""
                           SELECT ?prop ?cla
            	                WHERE { ?prop owl:equivalentClass ?cla }
                    """))

    for elem in equivalent_list:
        liste_triple.append([elem[0], 'equivalentClass', elem[1]])

    return liste_triple

def main():

    # load the ontology
    get_ontology(ONTOLOGY).load()

    '''

    chess = graph(name="chess")

    generate_all_classes(chess)
    generate_all_individuals(chess)
    generate_all_subclass_properties(chess)

    # TRY TO PRINT PIECES SUBCLASSES
    pieces_iri = "Chess_Ontology.Pieces"
    pieces_classe = chess.get_classes()[pieces_iri]
    
    '''
    
    subclasses = generate_triple_list_subclass()

    individuals = generate_triple_list_individuals()

    properties = generate_triple_list_object_properties()

    equivalent = generate_triple_list_equivalent()

    if PRINT_INFO:
        # TRY TO PRINT ALL GRAPH INFO
        #chess.print_all()

        print()
        print("====================================================================")
        print("====================================================================")

        # TRY TO PRINT PIECES SUBCLASSES
        #pieces_classe.print_all()

        print()
        print("====================================================================")
        print("===================  SUBCLASS TRIPLES ===================")
        print("====================================================================")

        # TRY TO PRINT TRIPLE_LIST FOR SUBCLASS
        for t in subclasses:
            print(t)

        print()
        print("====================================================================")
        print("===================  INDIVIDUALS TRIPLES ===================")
        print("====================================================================")

        # TRY TO PRINT TRIPLE_LIST FOR INDIVIDUALS
        for t in individuals:
            print(t)


        print()
        print("====================================================================")
        print("===================  PROPERTIES TRIPLES ===================")
        print("====================================================================")

        # TRY TO PRINT TRIPLE_LIST FOR PROPERTIES
        for t in properties:
            print(t)

        print()
        print("====================================================================")
        print("===================  EQUIVALENT CLASS ===================")
        print("====================================================================")

        # TRY TO PRINT TRIPLE_LIST FOR PROPERTIES
        for t in equivalent:
            print(t)

    if CREATE_OUTPUT:
        # create output (it should not exist)
        output = open("output/output_" + ONTOLOGY_NAME, "w", encoding="utf-8")

        rdf_triple_template_file = open("resource/template/rdf_triple.txt")
        rdf_triple_template = string.Template(rdf_triple_template_file.read())

        for t in subclasses:
            output_string = rdf_triple_template.substitute(subject=t[0], predicate=t[1], object=t[2])
            output.write(output_string)

        for t in individuals:
            output_string = rdf_triple_template.substitute(subject=t[0], predicate=t[1], object=t[2])
            output.write(output_string)

        for t in properties:
            output_string = rdf_triple_template.substitute(subject=t[0], predicate=t[1], object=t[2])
            output.write(output_string)

        for t in equivalent:
            output_string = rdf_triple_template.substitute(subject=t[0], predicate=t[1], object=t[2])
            output.write(output_string)

        rdf_triple_template_file.close()
        output.close()

if __name__ == '__main__':
    main()
