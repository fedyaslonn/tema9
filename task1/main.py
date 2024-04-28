import os

print(f"Имя ОС {os.name}")

print(f"Текущая директория {os.getcwd()}")

if not os.path.join("txtfiles"):
    os.mkdir("txtfiles")
txt_path = 'txtfiles'

n = int(input("Введите количество создаваемых файлов "))


for i in range(1, n+1):
    create_txt_file = f'example{i}.txt'
    if not os.path.exists(create_txt_file):
        with open(create_txt_file, 'w', encoding='utf-8') as file:
            file.write(f'Hello! File name {create_txt_file}')

files_data = {}
for file in os.listdir():
    if file.endswith('.txt'):
        if '.txt' not in files_data:
            files_data['.txt'] = []
        files_data['.txt'].append(file)


for file in os.listdir():
    if file in files_data['.txt']:
        os.replace(file, os.path.join(txt_path, file))

num = 0
tot_size = 0
for file in os.listdir(txt_path):
    num += 1
    tot_size += os.stat(os.path.join(txt_path, file)).st_size
print(f"В папке с текстовыми файлами перемещено {num} файлов, их суммарный размер {tot_size}")


while True:
    old_file = input("Введите название старого файла: ")
    if old_file == 'quit':
        print(f"Завершение работы")
        break
    if old_file in os.listdir(txt_path):
        for i, file in enumerate(os.listdir(txt_path), start=1):
            new_file = f'renamed_file{i}.txt'
            if new_file not in os.listdir(txt_path):
                os.rename(os.path.join(txt_path, old_file), os.path.join(txt_path, new_file))
                print(f"Файл {old_file} был переименован в {new_file}")
                break
        else:
            print(f"Файл с таким именем уже существует")
            break
    else:
        print(f"Файл {old_file} не найден в папке {txt_path}")