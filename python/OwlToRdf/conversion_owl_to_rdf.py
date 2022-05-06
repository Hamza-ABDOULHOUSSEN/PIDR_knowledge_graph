from owlready2 import *
import sys
import os
import string

def reasoner(ONTOLOGY, ONTOLOGY_AFTER_REASONER):
    onto=get_ontology(ONTOLOGY).load()
    with onto:
        sync_reasoner()
        onto.save(file=ONTOLOGY_AFTER_REASONER)

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

    # this request generate all pairs of iri (cla1, cla2) where cla1 is equivalent to cla2
    equivalent_list = list(default_world.sparql("""
                           SELECT ?cla1 ?cla2
            	                WHERE { ?cla1 owl:equivalentClass ?cla2 }
                    """))

    for (cla1, cla2) in equivalent_list:
        cla1 = str(cla1)
        cla2 = str(cla2)
        liste_triple.append((cla1, 'equivalentClass', cla2))

    return liste_triple

def remove_restriction(triples):
    list_of_restrictions = [' & ', ' | ', 'Not(', 'some(', 'only(', 'value(', 'min(', 'max(']

    new_triples = []

    for triple in triples:
        add = True
        for elem in triple:
            for restr in list_of_restrictions:

                if restr in elem:
                    add = False

        if add:
            new_triples.append(triple)

    return new_triples

def print_info(subclasses, individuals, properties, equivalent):
    # TRY TO PRINT ALL GRAPH INFO
    # chess.print_all()

    print()
    print("====================================================================")
    print("====================================================================")

    # TRY TO PRINT PIECES SUBCLASSES
    # pieces_classe.print_all()

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

def create_output(OUTPUT_FILE, subclasses, individuals, properties, equivalent):
    # create output (it should not exist)
    output = open(OUTPUT_FILE, "w", encoding="utf-8")

    # HEADER
    with open("resource/template/header.txt", "r") as header:
        output.write(header.read())

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

    # FOOTER
    with open("resource/template/footer.txt") as footer:
        output.write(footer.read())

    output.close()

def main():
    
    ONTOLOGY_NAME = "pizza"
    DEFAULT = 0     # 1 to use the script as it should be in default

    PRINT_INFO = 0  # 0 for no and 1 for yes
    ONTOLOGY = f"resource/{ONTOLOGY_NAME}.owl"
    CREATE_OUTPUT = 1  # 0 for no and 1 for yes
    STANDART_OUTPUT = 1
    OUTPUT_FILE = f"output/standard_{ONTOLOGY_NAME}.xml"
    REASONER = 1  # 0 for no and 1 for yes
    KEEP_REASONER_FILE = 1  # 0 for no and 1 for yes
    ONTOLOGY_AFTER_REASONER = f"resource/reasoner/{ONTOLOGY_NAME}.owl"

    if DEFAULT:
        PRINT_INFO = 0
        ONTOLOGY = ""
        CREATE_OUTPUT = 0
        STANDART_OUTPUT = 0
        OUTPUT_FILE = ""
        REASONER = 0
        KEEP_REASONER_FILE = 0
        ONTOLOGY_AFTER_REASONER = ""

        if "-i" not in sys.argv:
            raise Exception("the input ontology is required with -i option")


    # Command Line parameters
    sys.argc = len(sys.argv)

    for i in range(sys.argc):
        if sys.argv[i] == "-p":
            PRINT_INFO = 1
        elif sys.argv[i] == "-i":
            i = i + 1
            ONTOLOGY = sys.argv[i]
            OUTPUT_FILE = ONTOLOGY[:-4] + '_output'
        elif sys.argv[i] == "-o":
            i = i + 1
            CREATE_OUTPUT = 1
            OUTPUT_FILE = sys.argv[i]
            if os.path.exists(OUTPUT_FILE):
                raise Exception("Output file already exists (use -O to overwrite)")
        elif sys.argv[i] == "-O":
            i = i + 1
            CREATE_OUTPUT = 1
            OUTPUT_FILE = sys.argv[i]
        elif sys.argv[i] == "-r":
            REASONER = 1
            ONTOLOGY_AFTER_REASONER = ONTOLOGY[:-4] + "_reasoner_temp.owl"
        elif sys.argv[i] == "-kr":
            i = i+1
            KEEP_REASONER = 1
            ONTOLOGY_AFTER_REASONER = sys.argv[i]
            if os.path.exists(ONTOLOGY_AFTER_REASONER):
                raise Exception("File after reasoner already exists (use -Kr to overwrite)")
        elif sys.argv[i] == "-Kr":
            i = i + 1
            KEEP_REASONER = 1
            ONTOLOGY_AFTER_REASONER = sys.argv[i]

    # check for exception
    if not os.path.exists(ONTOLOGY):
        raise Exception("Input ontology does not exist")
    if ONTOLOGY[-4:] != '.owl':
        raise Exception("Input ontology is not an owl file (the extension is not .owl)")


    if REASONER:
        # launch the reasoner
        reasoner(ONTOLOGY, ONTOLOGY_AFTER_REASONER)

        # remove the previous ontology
        get_ontology(ONTOLOGY).destroy()

        ONTOLOGY = ONTOLOGY_AFTER_REASONER

    # load the ontology
    get_ontology(ONTOLOGY).load()

    subclasses = generate_triple_list_subclass()

    individuals = generate_triple_list_individuals()

    properties = generate_triple_list_object_properties()

    equivalent = generate_triple_list_equivalent()

    if STANDART_OUTPUT:
        subclasses = remove_restriction(subclasses)
        individuals = remove_restriction(individuals)
        properties = remove_restriction(properties)
        equivalent = remove_restriction(equivalent)

    if PRINT_INFO:
        print_info(subclasses, individuals, properties, equivalent)

    if CREATE_OUTPUT:
        create_output(OUTPUT_FILE, subclasses, individuals, properties, equivalent)

    # delete the temporary reasoner file
    if REASONER and not KEEP_REASONER_FILE:
        os.remove(ONTOLOGY_AFTER_REASONER)

if __name__ == '__main__':
    main()
