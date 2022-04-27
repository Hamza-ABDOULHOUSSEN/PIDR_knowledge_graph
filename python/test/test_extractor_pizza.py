import pytest
from OwlToPythonClass.extractor import *
import os

ONTOLOGY = "file://resource/pizza.owl"
BASE = "file://resource/"

# searching for all ontologies
ALL_ONTOLOGIES = os.listdir("resource")
for ELEM in ALL_ONTOLOGIES:
    if not(ELEM[-4:] == ".owl"):
        ALL_ONTOLOGIES.remove(ELEM)

### load the ontology
# removing previous ontologies loaded
for ONTO in ALL_ONTOLOGIES:
    get_ontology(BASE+ONTO).destroy()

get_ontology(ONTOLOGY).load()


subclasses = generate_triple_list_subclass()
properties = generate_triple_list_object_properties()
individuals = generate_triple_list_individuals()

def test_subclass():
    assert len(subclasses) == 259
    assert ('pizza.SpinachTopping', 'subClassOf', 'pizza.VegetableTopping') in subclasses


def test_individuals():
    assert len(individuals) == 5
    assert ("pizza.France", "individualOf", "pizza.Country") in individuals

    ## get individual list
    individual_list = []
    for t in individuals:
        individual_list.append(t[2])

    assert 'pizza.Food' not in individual_list