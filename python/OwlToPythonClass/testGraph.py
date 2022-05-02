from rdflib import Graph
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot

path = "owl_object_diagram/owl_object.png"

def visualize(g):
    stream = io.StringIO()
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    png = dg.create_png()
    display(Image(png))

def vis():
    display(Image(path))

g = Graph()

result = g.parse("./../output/output_pizza_some.xml")
v = g.serialize(format="xml")

path = "image.png"

#visualize(g)
vis()