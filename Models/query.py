import re
from functools import *

with open('./Input/database.txt', 'r') as f:
    database = []
    for row in f.readlines():
        database.append(row if row[-1] != '\n' else row[:-1])

def query(ps):
    first = ps.index(' ')
    second = ps.index('(', first)

    query_command = ps[:first]
    query_variable = ps[first+1:second-1].split()
    query_tables = ps[second:].split('(')
    query_tables = [table[:-1].split() for table in query_tables]

    normalize_city = {'Đà_Nẵng': 'DANANG', 'Hồ_Chí_Minh': 'HCMC', 'HCM': 'HCMC', 'Huế': 'HUE', 'Hà_Nội': 'HN', 'Nha_Trang': 'NTrang'}
    for table in query_tables:
        for field, index in zip(table, range(len(table))):
            if field in normalize_city:
                table[index] = normalize_city[field]
            regex = r"[0-9]{3,4}HR"
            if re.search(regex, field):
                table[index] = field[:-4] + ':' + field[-4:]

    results = []

    if query_command == "PRINT-ALL":
        for table in query_tables:
            if len(table) == 0:
                continue

            result = []
            all_unmatch = True
            for row in database:
                row = row[1:-1].split()
                unmatch = False
                is_append = False
                for column, field in zip(row, table):
                    if column != field:
                        if field[0] != '?':
                            unmatch = True
                            break
                        elif field in query_variable:
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
        for table in query_tables:
            if len(table) == 0:
                continue

            all_unmatch = True
            for row in database:
                match = 0
                row = row[1:-1].split()
                for column, field in zip(row, table):
                    if column == field:
                        match += 1
                if match == len(table):
                    results = ['Có']
                    break

    fileName = "./Output/output_f.txt"
    output = open(fileName,"a")
    output.write(str(', '.join(results)))
    output.write("\n")

    return results