from termcolor import colored

class classe:
    def __init__(self, iri, name):
        self.iri = iri
        self.name = name
        self.subclasses = {}

    def get_iri(self):
        return self.iri

    def get_name(self):
        return self.name

    def add_subclass(self, classe):
        self.subclasses[classe.get_name()] = classe

    def get_subclasses(self):
        return self.subclasses

    def print_all(self):
        print(f"##### --- CLASSE : {self.name} --- #####")
        print()

        print("##### --- SUBCLASSES --- #####")
        for iri in self.subclasses.keys():
            print(f"{iri} : {self.subclasses[iri].get_name()}")
        n=len(self.subclasses)
        print(colored(f"{n} subclasses",'red'))
        print()

class individual:
    def __init__(self, iri, name):
        self.iri = iri
        self.name = name

    def get_iri(self):
        return self.iri

    def get_name(self):
        return self.name

class graph:
    def __init__(self, name):
        self.name = name
        self.classes = {}
        self.individuals = {}

    def get_name(self):
        return self.name

    def get_classes(self):
        return self.classes

    def get_individuals(self):
        return self.individuals

    def add_classe(self, classe):
        self.classes[classe.get_iri()] = classe

    def add_new_classe(self, iri, name):
        c = classe(iri=iri, name=name)
        self.classes[iri] = c

    def add_individual(self, individual):
        self.individuals[individual.get_iri()] = individual

    def add_new_individual(self, iri, name):
        ind = individual(iri=iri, name=name)
        self.individuals[iri] = ind

    def print_all(self):
        print(f"##### --- GRAPH : {self.name} --- #####")
        print()

        print("##### --- CLASSSES --- #####")
        for iri in self.classes.keys():
            print(f"{iri} : {self.classes[iri].get_name()}")
        n=len(self.classes)
        print(colored(f"{n} classes",'red'))
        print()

        print("##### --- INDIVIDUALS --- #####")
        for iri in self.individuals.keys():
            print(f"{iri} : {self.individuals[iri].get_name()}")
        n=len(self.individuals)
        print(colored(f"{n} individuals", 'red'))
        print()

