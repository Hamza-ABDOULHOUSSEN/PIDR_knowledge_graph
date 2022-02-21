from owlready import *

onto = Ontology("Chess Ontology.owl")
rank_list=['a','b','c','d','e','f','g','h']
class conditions(Thing):
    ontology = onto
    def check_out_the_board(self):
        if self.file<=0 or self.file>=9:
            return "false"
        if self.rank not in rank_list:
            return "false"
        else:
            return "true"


class has_file(FunctionalProperty):
    ontology = onto
    domain = [conditions]
    range = [int]
ANNOTATIONS[has_file]["python_name"] = "file"

class has_rank(FunctionalProperty):
    ontology = onto
    domain = [conditions]
    range = [str]
ANNOTATIONS[has_rank]["python_name"] = "rank"

my_test = conditions("my_drug", file=4,  rank= 'c')
print(my_test.check_out_the_board())
