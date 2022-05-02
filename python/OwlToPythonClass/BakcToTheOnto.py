from owlready2 import *
import string
from OwlToPythonClass.owl_object import *


ONTOLOGY = "file://resource/pizza.owl"
ONTOLOGY_NAME = "pizza"
PRINT_INFO = 1         # 0 for no and 1 for yes
CREATE_OUTPUT = 1         # 0 for no and 1 for yes

#for the comparison at the end

def buildClasses():

def buildIndivuals():

def buildObjectProperties():

def buildAnnotationProperties():

def buildAxioms():


def main():
    ontology = open("./output/output_pizza", "r", encoding="utf-8")
    new_ont=open("./output/new_pizza.owl", "w+", encoding="utf-8")
    k = 0
    lines = ontology.readlines()

    end=len(lines)
    for line in lines:
        if(line.startswith("<rdf:Description")):
            if(line.startswith("<ex:subClassOf>")):



    # Indivuals_find = False
    # lines = ontology.readlines()
    #
    # # copy of the code until the individuals part
    # while not Indivuals_find:
    #     line = lines[k]
    #     line_words = line.split(' ')
    #
    #     if "<owl:NamedIndividual" in line_words:
    #         Indivuals_find = True
    #     else:
    #         new_ontology.write(line)
    #         k += 1
    #
    # # add new match
    # print()
    # match_name = input("Match name : ")
    # match = generate_match_to_owl(match_name)
    # new_ontology.write(match)
    #
    # end_input = False
    #
    # num = 1
    # while not (end_input):
    #     print()
    #     piece = input("Piece : ")
    #     square = input("Square : ")
    #     file = square[0]
    #     rank = square[1]
    #     # description = input("Description : ")
    #
    #     next_move = input("Next move (press 'no' to end) : ")
    #
    #     if next_move == "no":
    #         end_input = True
    #         match_move = generate_last_match_move_to_owl(str(num), match_name, piece, square)
    #
    #     else:
    #         match_move = generate_match_move_to_owl(str(num), match_name, piece, square, str(num + 1))
    #
    #     new_ontology.write(match_move)
    #
    #     num += 1
    #
    # # add the rest of the code
    # n = len(lines)
    # while k != n:
    #     line = lines[k]
    #     new_ontology.write(line)
    #     k += 1
    #
    # ontology.close()
    # new_ontology.close()


if __name__ == '__main__':
    main()
