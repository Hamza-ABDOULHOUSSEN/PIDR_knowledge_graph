from owlready2 import *
import string
from OwlToPythonClass.owl_object import *
ONTOLOGY = "file://resource/pizza_some.owl"
ONTOLOGY_NAME = "pizza_some"

def main():

    # load the ontology
    onto=get_ontology(ONTOLOGY).load()
    with onto:
        sync_reasoner()
        onto.save(file="./resource/rules.owl")

if __name__ == '__main__':
    main()