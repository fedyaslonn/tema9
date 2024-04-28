def foo(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    with open (output_file, 'w') as f:
        for line in lines:
            new_line = line.split()
            if new_line[2] in "012":
                f.write(f"{new_line[0]} {new_line[1]} \n")




foo('input.txt', 'output.txt')