from owlready2 import *
import string
from OwlToPythonClass.owl_object import *


#list_of_predicate_reading=["individualOf","subClassOf","equivalentClass"]

#for the comparison at the end

# def buildClasses(subject,object):
#     with open("./output/new_pizza.owl", "w+", encoding="utf-8") as new_ont:
#
#         lines=new_ont.readlines()
#         alreay_exist=False
#         for line in lines:
#             if line.startswith("<owl:Class rdf:about=\"#"+subject+"\">"):
#                 new_ont.write("\n")
#                 new_ont.write("  <rdfs:subClassOf rdf:resource=\"#"+object+"\"/>\n") #check a mon avis n'ecrit pas au bon endroit !
#                 alreay_exist=True
#         if not (alreay_exist):
#             buildfirst="<owl:Class rdf:about=\"#"+subject+"\">"
#             new_ont.write(buildfirst)
#             new_ont.write("\n")
#             subclass="  <rdfs:subClassOf rdf:resource=\"#"+object+"\"/>"
#             new_ont.write(subclass)
#             new_ont.write("\n")
#             new_ont.write("</owl:Class>")
#             new_ont.write("\n")



# def buildIndivuals(subject,object):
#     with open("./output/new_pizza.owl", "w+", encoding="utf-8") as new_ont:
#         buildfirst="<"+object +" rdf:about=\"#"+subject+" \">"+"\n"
#         new_ont.write(buildfirst)
#         type="  <rdf:type rdf:resource=\"http://www.w3.org/2002/07/owl#NamedIndividual\"/>\n"
#         new_ont.write(type)
#         new_ont.write("</"+object+">")
# def buildObjectProperties():
#
# def buildAnnotationProperties():
#

link="./output/output_pizza.xml"
lenght_link= len(link.split("/"))
name_file=link.split("/")[lenght_link-1]
#express the name of the file that we have in all rdf:about

file_name_reduce=name_file.split('.')[0].removeprefix('output_')
file_path="http://www.semanticweb.org/hamza/ontologies/2022/3/pizza"
def main():
    with open("./output/new_pizza2.owl", "w+", encoding="utf-8") as new_ont:
        #header
        new_ont.write("<?xml version=\"1.0\"?>\n")
        new_ont.write("<rdf:RDF xmlns=\""+file_path+"#\"\n "
                      "xml:base=\""+file_path+"\" \n "
                      "xmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n "
                      "xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n "
                      "xmlns:xml=\"http://www.w3.org/XML/1998/namespace\"\n "
                      "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n "
                      "xmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n "
                      "xmlns:"+file_name_reduce+"=\""+file_path+"#\">\n "
                      "<owl:Ontology rdf:about=\""+file_path+""
                      "\"/>\n\n\n")

        triples=gettriples2()
        for triple in triples:
            print(triple)
            object=triple[2]
            subject=triple[0]
            if(triple[1].startswith(file_name_reduce)):
                name_properties=triple[1].split(".")[1]
                name_range=triple[2].split(".")[1]
                name_domain=triple[0].split(".")[1]
                buildfirst="<owl:ObjectProperty rdf:about=\""+file_path+"#"+name_properties+"\">\n"
                new_ont.write(buildfirst)
                domain="    <rdfs:domain rdf:resource=\""+file_path+"#"+name_domain+"\"/>\n"
                new_ont.write(domain)
                range="    <rdfs:range rdf:resource=\""+file_path+"#"+name_range+"\"/>\n"
                new_ont.write(range)
                new_ont.write("</owl:ObjectProperty>\n")
                new_ont.write("\n")
            if(triple[1]=="subClassOf"):
                lines = new_ont.readlines()
                alreay_exist = False
                for line in lines:
                    if line.startswith("<owl:Class rdf:about=\""+file_path+"#" + subject + "\">"):
                        new_ont.write("\n")
                        name_object = triple[2].split(".")[1]
                        new_ont.write(
                            "  <rdfs:subClassOf rdf:resource=\""+file_path+"#" + name_object + "\"/>\n")  # check a mon avis n'ecrit pas au bon endroit !
                        alreay_exist = True
                if not (alreay_exist):
                    name_subject=triple[0].split(".")[1]
                    if(triple[2]=="Thing"):
                        name_object=file_name_reduce+"."+triple[2]
                        name_subject=triple[0].split(".")[1]
                        build="<owl:Class rdf:about=\""+file_path+"#"+name_subject+"\"/>"
                        new_ont.write(build)
                    else:
                        name_object = triple[2].split(".")[1]
                        buildfirst = "<owl:Class rdf:about=\""+file_path+"#" + name_subject + "\">"
                        new_ont.write(buildfirst)
                        new_ont.write("\n")
                        subclass = "  <rdfs:subClassOf rdf:resource=\""+file_path+"#" + name_object + "\"/>"
                        new_ont.write(subclass)
                        new_ont.write("\n")
                        new_ont.write("</owl:Class>")
                    new_ont.write("\n")
                    new_ont.write("\n")

                #buildClasses(triple[1],triple[2])
            if(triple[1]=="individualOf"):
                #version1 didn't load in protégé
                # name_subject = triple[0].split(".")[1]
                # name_object = triple[2].split(".")[1]
                # buildfirst = "<" + object + " rdf:about=\""+file_path+"#" + name_subject + " \">" + "\n"
                # new_ont.write(buildfirst)
                # type = "  <rdf:type rdf:resource=\"http://www.w3.org/2002/07/owl#NamedIndividual\"/>\n"
                # new_ont.write(type)
                # new_ont.write("</" + name_object + ">")
                # new_ont.write("\n")
                # new_ont.write("\n")
                #version2 :
                name_subject = triple[0].split(".")[1]
                name_object = triple[2].split(".")[1]
                buildfirst="<owl:NamedIndividual rdf:about=\""+file_path+"#"+name_subject+"\">\n"
                new_ont.write(buildfirst)
                type="    <rdf:type rdf:resource=\""+file_path+"#"+name_object+"\"/>\n"
                new_ont.write(type)
                new_ont.write("</owl:NamedIndividual>\n")
                new_ont.write("\n")
                new_ont.write("\n")
                #buildIndivuals(triple[1],triple[2])
        new_ont.write("</rdf:RDF>")







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

def gettriples2():
    INPUT_FILE = "output/output_pizza.xml"
    file = open(INPUT_FILE, "r", encoding="utf-8")
    lines = file.readlines()
    k = 0
    n = len(lines)

    triple_list = []

    pattern_subject = r'<rdf:Description rdf:about="(?P<subject>.*)">'
    pattern_predicate = r'    <ex:(?P<predicate>.*)>'
    pattern_object = r'         <rdf:Description rdf:about="(?P<object>.*)"/>'

    while k < n:
        line = lines[k]

        if line.startswith("<rdf:Description "):
            value = line
            m = re.match(pattern_subject, value)
            subject = m.group("subject")
            k += 1
            line = lines[k]
            value = line
            m = re.match(pattern_predicate, value)
            predicate = m.group("predicate")
            k += 1
            line = lines[k]
            value = line
            m = re.match(pattern_object, value)
            object = m.group("object")

            triple_list.append((subject, predicate, object))


        k = k+1

    file.close()

    #print(len(triple_list))
    return triple_list


if __name__ == '__main__':
    main()
