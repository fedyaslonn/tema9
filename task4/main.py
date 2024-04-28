def read_words(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        words = file.read().split()
        words = [word.strip().lower() for word in words]
    return words

def replace_substr(line, worlds_to_replace_set):
    for word in worlds_to_replace_set:
        index = line.lower().find(word)
        while index != -1:
            line = line[:index] + '*' * len(word) + line[index+len(word):]
            index = line.lower().find(word, index + len(word))
    return line
def replace_words(filename, file_to_read, file_to_write):
    words_to_replace = read_words(filename)
    words_to_replace_set = set(words_to_replace)

    with open(file_to_read, 'r', encoding='UTF-8') as file:
        lines = file.readlines()


    with open(file_to_write, 'w', encoding='UTF-8') as new_file:
        for line in lines:
            res_line = replace_substr(line, words_to_replace_set)
            new_file.write(res_line)

tot_res = replace_words('read.txt', 'input.txt', 'output.txt')