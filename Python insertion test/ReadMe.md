# 1. Python insertion in owl

This folder contains a python script that insert matches in the chess ontology


- [1. Python insertion in owl](#1-python-insertion-in-owl)
  - [1.1. Prepare the ontolgy](#11-prepare-the-ontolgy)
  - [1.2. Commands](#12-commands)
  - [1.3. Exemple of inputs](#13-exemple-of-inputs)
  - [1.4. New output](#14-new-output)


## 1.1. Prepare the ontolgy

- The script will take `Chess Ontology.owl`and insert matches into this ontology  
- It create a new ontology with adds : `Chess Ontology new_version.owl`  
- <span style="color:red">delete the file `Chess Ontology new_version.owl` before using the script</span>.

## 1.2. Commands

To use the script, open a terminal in this folder (`Python insertion test`) and launch the command

```
python3 match_insertion.py
```

Complete the input to add a match  
  
To end the inputs, write no after Next Move :
```
Next move (press 'no' to end) : no
```


## 1.3. Exemple of inputs
To hade the Scholar's mate in the ontology

```
Match name : Scholar_mate
```

```
Piece : p2e
Square : e4
Description : Double_Forward
Next move (press 'no' to end) : 
```

```
Piece : p7e
Square : e5
Description : Double_Forward
Next move (press 'no' to end) : 
```

```
Piece : 1C_Bishop_w
Square : c4
Description : move_in_diagonal
Next move (press 'no' to end) : 
```

```
Piece : 8B_Knight_b
Square : c6
Description : move_in_L_2_square_height_and_1_square_width              
Next move (press 'no' to end) : 
```

```
Piece : White_queen
Square : h5
Description : move_in_diagonal
Next move (press 'no' to end) : 
```

```
Piece : 8G_Knight_b
Square : f6
Description : move_in_L_2_square_height_and_1_square_width
Next move (press 'no' to end) : 
```

```
Piece : White_queen
Square : f7
Description : move_in_diagonal
Next move (press 'no' to end) : no
```

## 1.4. New output
the ontology with the match inserted is in `Chess Ontology new_version.owl`. You can check if the match has been correctly added.
