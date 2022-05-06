# 1. conversion_owl_to_rdf

- [1. conversion_owl_to_rdf](#1-conversion_owl_to_rdf)
  - [1.1. Run](#11-run)
  - [1.2. Command line option](#12-command-line-option)
  - [1.3. Complete example](#13-complete-example)


This script take a owl file, print information and create an rdf file

## 1.1. Run
from `python` directory
```
PYTHONPATH=. python3 OwlToRdf/conversion_owl_to_rdf.py
```

## 1.2. Command line option
```     
DESCRIPTION

     -i      [required] [need argument] it is to add the owl input file path
             by default, the output is the input with '_output'
             ex : -i "resource/pizza.owl"  
             
         
     -o      [need argument] add the output file path
             ex : -o "output/pizza"  
             

     -O      [need argument] same as -O but overwrite the file if already exists
             ex : -O "output/pizza"      
             

     -p      To print the triple added
     

     -s      To create standard triple without restrictions
     
     -r      To add reasoner before
     

     -kr     [need argument] To keep the ontology made after the reasoner
             the argument is the path of the new file
             ex : -kr "reasoner/pizza.owl" 
             
             
     -Kr     [need argument] same as -kr but overwrite the file if already exists
             ex : -Kr "reasoner/pizza.owl"               
               
```

## 1.3. Complete example

```
PYTHONPATH=. python3 OwlToRdf/conversion_owl_to_rdf.py -i "resource/pizza.owl" -o "bla" -p
```
