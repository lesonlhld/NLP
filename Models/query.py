import re
from functools import *

with open('./Input/database.txt', 'r') as f:
    database = []
    for row in f.readlines():
        database.append(row if row[-1] != '\n' else row[:-1])

def query(ps):
    first = ps.index(' ')
    second = ps.index('(', first)

    command = ps[:first]
    variables = ps[first+1:second-1].split()
    data = ps[second:].replace("(","").replace(")","").split(' ')

    convert_name = {'Đà_Nẵng': 'DANANG', 'Hồ_Chí_Minh': 'HCMC', 'HCM': 'HCMC', 'Huế': 'HUE', 'Hà_Nội': 'HN', 'Nha_Trang': 'NTrang'}
    for field, index in zip(data, range(len(data))):
        if field in convert_name:
            data[index] = convert_name[field]
        regex = r"[0-9]{3,4}HR"
        if re.search(regex, field):
            data[index] = field[:-4] + ':' + field[-4:]

    results = []

    if command == "PRINT-ALL":
        result = []
        all_unmatch = True
        for row in database:
            row = row[1:-1].split()
            unmatch = False
            is_append = False
            for column, field in zip(row, data):
                if column != field:
                    if field[0] != '?':
                        unmatch = True
                        break
                    elif field in variables:
                        result.append(column)
                        is_append = True

            if unmatch and is_append:
                result.pop()
            all_unmatch = all_unmatch and unmatch

        if all_unmatch:
            results = []

        if len(result) != 0:
            results.append(result)
        results = list(reduce(lambda a, b: set(a) & set(b), results))
    else:
        results = ['Không']
        all_unmatch = True
        for row in database:
            match = 0
            row = row[1:-1].split()
            for column, field in zip(row, data):
                if column == field:
                    match += 1
            if match == len(data):
                results = ['Có']
                break

    fileName = "./Output/output_f.txt"
    output = open(fileName,"a")
    output.write(str(', '.join(results)))
    output.write("\n")

    return results