
def main(): 

    file_name = input("Enter the renderdoc file")

    file = open(file_name, "r")
    csv_file = open(file_name + ".csv", "w")
    cout = 0

    for line in file: 
        cout += 1

        line = line.strip()

        raw_csv_arguments = line.rsplit(", ")

        if cout == 1: 
            
            first_line = ""

            for idx, arguments in enumerate(raw_csv_arguments): 
                if idx == len(raw_csv_arguments) -1:
                    first_line += arguments.partition(" ")[0] + "\n"
                else:
                    first_line += arguments.partition(" ")[0] + ","
            
            csv_file.write(first_line)

        data = ""

        for idx, arguments in enumerate(raw_csv_arguments): 
                if idx == len(raw_csv_arguments) -1:
                    data += arguments.partition(" ")[2] + "\n"
                else:
                    data += arguments.partition(" ")[2] + ","
            
        csv_file.write(data)
    
    file.close()
    csv_file.close()

if __name__ == "__main__":
    main()