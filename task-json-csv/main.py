import json
import csv
'''
8. JSON и CSV.
'''
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    with open(csv_file, mode='w', newline='', encoding="UTF-8") as w_file:
        names = ["name", "birthday", "height", "weight", "car", "languages"]
        file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for row in data:
            file_writer.writerow(row)


def read_json(json_file):
    with open(json_file, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for row in data:
            print(row)
def read_csv(csv_file):
    with open(csv_file, 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def add_to_json(json_file):
    name = str(input())
    birthday = str(input())
    height = int(input())
    weight = int(input())
    car = str(input())
    languages = str(input()).split(',')


    add_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }

    with open(json_file, 'r+', encoding="UTF-8") as file:
        data = json.load(file)
        data.append(add_employee)
        file.seek(0)
        json.dump(data, file, indent=4)

def add_to_csv(csv_file):
    name = str(input())
    birthday = str(input())
    height = int(input())
    weight = int(input())
    car = str(input())
    languages = str(input()).split(',')


    add_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }

    with open(csv_file, 'a', newline='', encoding="UTF-8") as w_file:
        names = ["name", "birthday", "height", "weight", "car", "languages"]
        file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writerow(add_employee)


def read_info(json_file):
    name = str(input())
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    for person in data:
        if person['name'] == name:
            return person


def filter_by_lang(json_file):
    lang = str(input())
    res = []
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    for person in data:
        if lang in person['languages']:
            res.append(person)
    return res

def filter_by_yera(json_file):
    year = str(input())
    tot_height = 0
    cnt = 0
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    for person in data:
        if int(person["birthday"].split(".")[-1]) < int(year):
            tot_height += person["height"]
            cnt += 1
    return tot_height/cnt



while True:
    print("\nМеню:")
    print("1. Прочитать данные и преобразовать JSON-файла")
    print("2. Сохранить данные в CSV-файл")
    print("3. Добавить нового сотрудника в JSON-файл")
    print("4. Добавить нового сотрудника в CSV-файл")
    print("5. Прочитать информацию о сотруднике по имени")
    print("6. Фильтр по языку")
    print("7. Фильтр по году")
    print("8. Выход")
    choice = input("Выберите действие: ")
    if choice == '1':
        read_json("json_file.json")
    elif choice == '2':
        read_csv("csv_file.csv")
    elif choice == '3':
        add_to_json("json_file.json")
    elif choice == '4':
        add_to_json("csv_file.csv")
    elif choice == '5':
        print(read_info("json_file.json"))
    elif choice == '6':
        print(filter_by_lang("json_file.json"))
    elif choice == '7':
        print(filter_by_yera("json_file.json"))
    else:
        break