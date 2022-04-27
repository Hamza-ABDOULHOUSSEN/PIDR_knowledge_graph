from rdflib import Graph
from rdflib.plugin import register, Serializer, Parser
g = Graph()
g.parse("https://raw.githubusercontent.com/Hamza-ABDOULHOUSSEN/PIDR_knowledge_graph/main/Chess_Ontology.owl?token=GHSAT0AAAAAABTBJMC4GG4VYLTUEXLH6QQCYSEPTPQ")
v = g.serialize(format="xml")

# g = Graph()
#
# g.parse("https://raw.githubusercontent.com/Hamza-ABDOULHOUSSEN/PIDR_knowledge_graph/main/Chess_Ontology.owl?token=GHSAT0AAAAAABTBJMC4GG4VYLTUEXLH6QQCYSEPTPQ")
# v = g.serialize(format="xml")
# print(len(g))