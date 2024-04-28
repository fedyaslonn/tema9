def foo(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    with open(output_file, 'w', encoding='UTF-8') as f:
        tot_res = []
        tot_res2 = []
        for line in lines:
            res = []
            words = line.split()
            for word in words:
                res.append(words.count(word))
            tot_res2.append(max(res))
            max_word = [word for word in words if words.count(word) == max(res)]
            tot_res.append(set(max_word))
        for i, j in zip(tot_res, tot_res2):
            f.write(f"Слово {i} - число повторений {j} \n")

foo('input.txt', 'output.txt')

