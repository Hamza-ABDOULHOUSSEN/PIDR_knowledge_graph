from termcolor import colored
from typing import Dict


class individual:
    def __init__(self, iri, name, parent_class):
        self.iri: str = iri
        self.name: str = name
        self.parent_class: classe = parent_class

    def get_iri(self):
        return self.iri

    def get_name(self):
        return self.name

    def get_parent_classe(self):
        return self.parent_class

    def print_all(self):
        print(f"##### --- INDIVIDUAL : {self.name} --- #####")
        print()

        print(f"iri : {self.iri}")
        print(f"parent_class : {self.parent_class.get_name()}")


class classe:
    def __init__(self, iri, name):
        self.iri: str = iri
        self.name: str = name
        self.subclasses: Dict[str, classe] = classe_dict()
        self.individuals: Dict[str, individual] = individual_dict()

    def get_iri(self):
        return self.iri

    def get_name(self):
        return self.name

    def get_subclasses(self):
        return self.subclasses

    def get_individuals(self):
        return self.individuals

    def add_subclass(self, classe):
        self.subclasses[classe.get_iri()] = classe

    def add_individual(self, individual):
        self.individuals[individual.get_iri()] = individual

    def print_all(self):
        print(f"##### --- CLASSE : {self.name} --- #####")
        print()

        print("##### --- SUBCLASSES --- #####")
        for iri in self.subclasses.keys():
            print(f"{iri} : {self.subclasses[iri].get_name()}")
        n = len(self.subclasses)
        print(colored(f"{n} subclasses", 'red'))
        print()

        print("##### --- INDIVIDUALS --- #####")
        for iri in self.individuals.keys():
            print(f"{iri} : {self.individuals[iri].get_name()}")
        n = len(self.individuals)
        print(colored(f"{n} individuals", 'red'))
        print()


class graph:
    def __init__(self, name):
        self.name: str = name
        self.classes: Dict[str, classe] = classe_dict()
        self.individuals: Dict[str, individual] = {}

    def get_name(self):
        return self.name

    def get_classes(self):
        return self.classes

    def get_individuals(self):
        return self.individuals

    def add_classe(self, classe):
        self.classes[classe.get_iri()] = classe

    def add_individual(self, individual):
        self.individuals[individual.get_iri()] = individual

    def print_all(self):
        print(f"##### --- GRAPH : {self.name} --- #####")
        print()

        print("##### --- CLASSSES --- #####")
        for iri in self.classes.keys():
            print(f"{iri} : {self.classes[iri].get_name()}")
        n = len(self.classes)
        print(colored(f"{n} classes", 'red'))
        print()

        print("##### --- INDIVIDUALS --- #####")
        for iri in self.individuals.keys():
            print(f"{iri} : {self.individuals[iri].get_name()}")
        n = len(self.individuals)
        print(colored(f"{n} individuals", 'red'))
        print()


## DICT CLASS TO CHECK FOR TYPES
class classe_dict(dict):
    self: Dict[str, classe]

    def __setitem__(self, key, val):
        if not isinstance(key, str):
            raise ValueError("key must be a str")
        if not isinstance(val, classe):
            raise ValueError("value must be a classe object")
        dict.__setitem__(self, key, val)

class individual_dict(dict):
    self: Dict[str, individual]

    def __setitem__(self, key, val):
        if not isinstance(key, str):
            raise ValueError("key must be a str")
        if not isinstance(val, individual):
            raise ValueError("value must be an individual object")
        dict.__setitem__(self, key, val)
