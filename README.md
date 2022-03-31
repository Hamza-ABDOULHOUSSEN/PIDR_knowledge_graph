# 1. PIDR_knowledge_graph

This projet as for objectives to develop an algorithm to pass from knowledge graph throught ontonlogy. At the end, we should be able to write a scientific article. Plus, if we have time, we will improve some algorithms that already exist.

- [1. PIDR_knowledge_graph](#1-pidr_knowledge_graph)
  - [1.1. tools and langage uses](#11-tools-and-langage-uses)
  - [1.2. content](#12-content)
    - [1.2.1. Meeting minutes](#121-meeting-minutes)
    - [1.2.2. Python insertion test](#122-python-insertion-test)
    - [1.2.3. python](#123-python)
    - [1.2.4. Chess Ontology.owl](#124-chess-ontologyowl)
  - [1.3. Workflows](#13-workflows)
  - [1.4. useful link and documents](#14-useful-link-and-documents)


## 1.1. tools and langage uses 

Our programation langage we use will be Python. For mor simplicity, we will use english in the entire project.

## 1.2. content

### 1.2.1. [Meeting minutes](Meeting%20Minutes)
This folder contains all the meeting minutes

### 1.2.2. [Python insertion test](Python%20insertion%20test)
This folder contains the python script to add match in the ontology

### 1.2.3. [python](python)
This folder contains the main python code, with the packages, the requirements and a test package which are lauched with pytest and automatically when we push on github.

### 1.2.4. Chess Ontology.owl
This is the ontology test created about chess knowledge

## 1.3. Workflows
In github we can also use workflows. We have made one which create a virtual machine, install python and add the requirements. Finally, it launch all the test with pytest.
At each push, the tests are launched automatically and we can see the results in the commit.

## 1.4. useful link and documents
- [Knowledge Graph Conferences](https://www.youtube.com/watch?v=bvwjG-3qAmY&list=PLDhh0lALedc7LC_5wpi5gDnPRnu1GSyRG)
- [Add VOWL dependencies for ontology visualizations](http://vowl.visualdataweb.org/protegevowl.html)
- [Chess Ontology online example](https://people.cs.ksu.edu/~hitzler/pub2/01-chess-example.pdf)
- [Python Chess library](https://python-chess.readthedocs.io/en/latest/)
- [Owlready documentation (ontology-oriented programming in Python)](https://pythonhosted.org/Owlready/index.html)
- [Chess documentation](https://en.wikipedia.org/wiki/Chess)
- [Neo4j create graph](https://neo4j.com/docs/graph-data-science/current/graph-create/)
- [Neo4j build graph from ontologies](https://neo4j.com/developer/graph-data-science/build-knowledge-graph-nlp-ontologies/)
- [Noe4j add ontologies](https://neo4j.com/labs/neosemantics/4.0/importing-ontologies/)
- [paper for constraint](https://alammehwish.github.io/dl4kg_eswc_2020/papers/paper3.pdf)
  
  
