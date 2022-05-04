from owlready2 import *
import string
from OwlToPythonClass.owl_object import *


ONTOLOGY = "file://resource/pizza.owl"
ONTOLOGY_NAME = "pizza"
PRINT_INFO = 1         # 0 for no and 1 for yes
CREATE_OUTPUT = 1         # 0 for no and 1 for yes


list_of_predicate_reading=["individualOf","subClassOf","equivalentClass"]

#for the comparison at the end

def buildClasses(subject,object):
    new_ont = open("./output/new_pizza.owl", "w+", encoding="utf-8")
    lines=new_ont.readlines()
    alreay_exist=False
    for line in lines:
        if line.startswith("<owl:Class rdf:about=\"#"+subject+"\">"):
            new_ont.write("\n")
            new_ont.write("  <rdfs:subClassOf rdf:resource=\"#"+object+"\"/>\n") #check a mon avis n'ecrit pas au bon endroit !
            alreay_exist=True
    if not (alreay_exist):
        buildfirst="<owl:Class rdf:about=\"#"+subject+"\">"
        new_ont.write(buildfirst)
        new_ont.write("\n")
        subclass="  <rdfs:subClassOf rdf:resource=\"#"+object+"\"/>"
        new_ont.write(subclass)
        new_ont.write("\n")
        new_ont.write("</owl:Class>")
        new_ont.write("\n")



def buildIndivuals(subject,object):
    #print("ohhhh")
    new_ont = open("./output/new_pizza.owl", "w+", encoding="utf-8")
    buildfirst="<"+object +"rdf:about=\"#"+subject+" \">"+"\n"
    new_ont.write(buildfirst)
    type="  <rdf:type rdf:resource=\"http://www.w3.org/2002/07/owl#NamedIndividual\"/>\n"
    new_ont.write(type)
    new_ont.write("</"+object+">")
# def buildObjectProperties():
#
# def buildAnnotationProperties():
#
# def buildAxioms():

link="./output/output_pizza_some.xml"
lenght_link= len(link.split("/"))
name_file=link.split("/")[lenght_link-1]
#express the name of the file that we have in all rdf:about

file_name_reduce=name_file.split('.')[0].removeprefix('output_')

def main():
    new_ont = open("./output/new_pizza.owl", "w+", encoding="utf-8")
    triples=gettriples()
    for triple in triples:
        #print(triple)
        if(triple[0]=="subClassOf"):
            buildClasses(triple[1],triple[2])
        if(triple[0]=="individualOf"):
            buildIndivuals(triple[1],triple[2])



def gettriples():
    ontology = open(link, "r", encoding="utf-8")
    lines = ontology.readlines()
    c = 0
    triples = []
    subjects = []
    objects = []
    call = 0
    for line in lines:

        type = -1
        if (line.startswith("<rdf:Description")):
            splLine = line.split("\"")
            subject = splLine[1]
            subject = subject.removeprefix(file_name_reduce + '.')
            subjects.append(subject)

        if (line.startswith("    <ex:subClassOf>")):
            type = 1
        if (line.startswith("    <ex:individualOf>")):
            type = 0
        if (line.startswith("    <ex:equivalentClass>")):
            type = 2
        if (line.startswith("         <rdf:Description")):
            c += 1
            object = line.split("\"")[1].removeprefix(file_name_reduce + '.')
            objects.append(object)
            call = 1

        if (type == 0 and call == 1):
            #triple="subject: "+subjects[c-1]+" predicate : "+"individualOf " + "object : "+ objects[c-1]
            triple=["individualOf",subjects[c-1],objects[c-1]]
            triples.append(triple)
            call = 0
        if (type == 1 and call == 1):
            #triple = "subject: " + subjects[c-1] + " predicate : " + "subClassOf " + "object : " + objects[c-1]
            triple = ["subClassOf", subjects[c - 1], objects[c - 1]]
            triples.append(triple)
            call = 0
        if (type == 2 and call == 1):
            #triple = "subject: " + subjects[c-1] + " predicate : " + "equivalentOf " + "object : " + objects[c-1]
            triple = ["equivalentOf", subjects[c - 1], objects[c - 1]]
            triples.append(triple)
            call = 0
    return triples





if __name__ == '__main__':
    main()
