from owlready2 import *
onto_path.append("/")
onto=get_ontology("Chess_Ontology.owl")
onto.load()
print(onto.classes())
good=list(onto.classes())
print(good)
onto.search(Make="*")
owlready_ontology=get_ontology("../Chess_Ontology_new_version.owl")
onto.imported_ontologies.append(owlready_ontology)
with onto:
    class TestAddClass(Thing):
        namespace=onto
        def IDontKnow(self):
            c=0
            for k in list(onto.classes()):
                c+= 1
            print("there is : " + c +" classes")

    myIndividual=TestAddClass("indiv1_test")
    print(myIndividual.name)


onto.save()