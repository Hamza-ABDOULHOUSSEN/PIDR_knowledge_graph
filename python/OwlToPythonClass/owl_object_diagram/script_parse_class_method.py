
def main():
    # also run the script from the directory python
    FILE = "OwlToPythonClass/owl_object.py"

    file = open(FILE, "r")

    lines = file.readlines()

    n = len(lines)
    k = 0
    first = True

    while k<n:
        line = lines[k]
        if line.startswith("class"):
            class_name = line.split(" ")[1][:-2]
            if first:
                print("###### X ######")
                print(f"class {class_name} " + "{")
                first = False
            else:
                print("}")
                print()
                print("###### X ######")
                print(f"class {class_name} " + "{")

        if line.startswith("    def __init__"):
            k += 1
            line = lines[k]
            while line.startswith("        self") and k<n:
                attr = line.split(" ")[8].split("self.")[1].replace(':', '')
                print(attr)
                k+=1
                line = lines[k]

            print("--")

        if line.startswith("    def"):
            method = line.split(" ", 5)[5][:-2].replace('self, ', '').replace('self', '')
            print(method)

        k += 1

    file.close()


if __name__ == '__main__':
    main()