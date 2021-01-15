import os
from research import Research
from collections import Counter
from filereader import FileReader
from dirreader import DirReader


def get_research(research):
    name_machines = {}
    for res in research:
        name = res.get_name()
        machine = res.get_machine()
        if name not in name_machines:
            name_machines[name] = [machine]
        else:
            name_machines[name].append(machine)
    return name_machines


def write_research(name_machines):
    file = open('research.txt', "w")
    for name in name_machines:
        file.write(name + ': ')
        machines = name_machines[name]
        c = Counter(machines)
        min_key = [k for k in c if all(c[m] >= c[k] for m in c)]
        file.write(str(min_key) + "\n")


def create_directory(path):
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
    except:
        print('Не удалось создать дирректорию')


def get_hours(research):
    hour_machines = {}
    for res in research:
        hour = res.get_hour()
        machine = res.get_machine()
        if hour not in hour_machines:
            hour_machines[hour] = [machine]
        else:
            hour_machines[hour].append(machine)
    return hour_machines


def write_hours(hour_machines):
    for hour in hour_machines:
        file = open(hour + '.txt', "w")
        file.write(hour + ': ')
        machines = hour_machines[hour]
        c = Counter(machines)
        for machines in c:
            file.write(str(machines) + ' (' + str(c[machines]) + '), ')


research = []

for file_name in DirReader("C:\\Users\\1\\PycharmProjects\\exam\\data"):
    with FileReader(file_name) as record_reader:
        for record in record_reader:
            record = record.split('\t')
            if len(record[4]) >= 50:
                research.append(Research(record[1], record[2], record[3], record[4]))

# Запись исследований каждого ученого
write_research(get_research(research))

# Создание директории
path_derectory = "C:\\Users\\1\\PycharmProjects\\exam\\hours"
create_directory(path_derectory)
os.chdir(path_derectory)

# Запись работы по часам
write_hours(get_hours(research))
