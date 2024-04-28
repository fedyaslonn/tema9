import re
def sum_numbers_in_string(input_string):
    nums = re.findall(r'\d+', input_string)
    tot_sum = sum(int(num) for num in nums)
    return tot_sum

input_string = "123 ааа456 1x2y3z 4 5 6"
res = sum_numbers_in_string(input_string)
print(f"Итоговая сумма: {res}")


