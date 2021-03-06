import pytest
from OwlToRdf.conversion_owl_to_rdf import *
import os

ONTOLOGY = "file://resource/Chess_Ontology.owl"

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

triple_list = generate_triple_list_subclass()
properties = generate_triple_list_object_properties()

def test_extractor_subclass():
    assert len(triple_list) == 18

    # get the list of pieces subclass
    sub_list = []
    for (a, _, b) in triple_list:
        if b == 'Chess_Ontology.Pieces':
            sub_list.append(a)

    assert len(sub_list) == 6
    assert 'Chess_Ontology.Rooks' in sub_list