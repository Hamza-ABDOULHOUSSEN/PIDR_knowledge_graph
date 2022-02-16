import string

# constant
line_to_write = 8    # the number of lines after the individual in the source code

# generate the owl code with the template for match_moves
def generate_match_move_to_owl(num, match_name, piece, cell, next_move_num):
    with open("template/match_move_template.owl") as t:
        template = string.Template(t.read())
        match_move = template.substitute(num=num, match_name=match_name, piece=piece, cell=cell, next_move_num=next_move_num)

    return match_move

def generate_last_match_move_to_owl(num, match_name, piece, cell):
    with open("template/last_match_move_template.owl") as t:
        template = string.Template(t.read())
        match_move = template.substitute(num=num, match_name=match_name, piece=piece, cell=cell)

    return match_move

# generate the owl code with the template for matches
def generate_match_to_owl(match_name):
    with open("template/match_template.owl") as t:
        template = string.Template(t.read())
        match = template.substitute(match_name=match_name)

    return match

# copy the code of the ontology and add the matches for each input
def main():
    ontology = open("Chess Ontology.owl", "r", encoding="utf-8")
    new_ontology = open("Chess Ontology new_version.owl", "w", encoding="utf-8")

    Indivuals_find = False
    line_after_individuals = 0

    k = 0
    lines = ontology.readlines()

    # copy of the code until the individuals part
    while line_after_individuals != line_to_write:
        line = lines[k]

        if line == "    // Individuals\n":
            Indivuals_find = True
        if Indivuals_find:
            line_after_individuals += 1
        
        new_ontology.write(line)
        k += 1

    # add new match
    print()
    match_name = input("Match name : ")
    match = generate_match_to_owl(match_name)
    new_ontology.write(match)

    end_input = False

    num = 1
    while not(end_input):
        print()
        piece = input("Piece : ")
        square = input("Square : ")
        file = square[0]
        rank = square[1]
        #description = input("Description : ")
        
        next_move = input("Next move (press 'no' to end) : ")

        if next_move == "no":
            end_input = True
            match_move = generate_last_match_move_to_owl(str(num), match_name, piece, square)

        else:
            match_move = generate_match_move_to_owl(str(num), match_name, piece, square, str(num+1))

        new_ontology.write(match_move)
        
        num+=1

    # add the rest of the code
    n = len(lines)
    while k != n:
        line = lines[k]
        new_ontology.write(line)
        k += 1


    ontology.close()
    new_ontology.close()


if __name__ == '__main__':
    main()


