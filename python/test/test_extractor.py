import pytest
from OwlToPythonClass.extractor import *

ONTOLOGY = "file://resource/Chess_Ontology.owl"

# load the ontology
get_ontology(ONTOLOGY).load()

chess = graph(name="chess")

generate_all_classes(chess)
generate_all_individuals(chess)
generate_all_subclass_properties(chess)

triple_list = generate_triple_list_subclass()
properties = generate_triple_list_object_properties()

def test_extractor_subclass():
    assert len(triple_list) == 26

    # get the list of pieces subclass
    sub_list = []
    for (a, _, b) in triple_list:
        if b == 'Chess_Ontology.Pieces':
            sub_list.append(a)

    assert len(sub_list) == 6
    assert 'Chess_Ontology.Rooks' in sub_list