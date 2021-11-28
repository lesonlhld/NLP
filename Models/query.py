import re
from functools import *
from Models.fileutil import load_file

# load dataset
train_dataset = load_file('./Input/train_dataset.txt')
attime_dataset = load_file('./Input/atime_dataset.txt')
dtime_dataset = load_file('./Input/dtime_dataset.txt')
runtime_dataset = load_file('./Input/runtime_dataset.txt')

def query(ps):
    # extract procedural semantic
    first_space = ps.index(' ')
    second_space = ps.index(' ', first_space+1)

    query_command = ps[:first_space]
    query_variable = ps[first_space+1:second_space]
    query_tables = ps[second_space+1:].split('(')
    query_tables = [table[:-1].split() for table in query_tables]

    # normalize query data
    normalize_city = {'Đà_Nẵng': 'DANANG', 'Hồ_Chí_Minh': 'HCMC', 'Huế': 'HUE', 'Hà_Nội': 'HN'}
    for table in query_tables:
        for field, index in zip(table, range(len(table))):
            # normalize city
            if field in normalize_city:
                table[index] = normalize_city[field]
            # normalize hours
            regex = r"[0-9]{3,4}HR"
            if re.search(regex, field):
                table[index] = field[:-4] + ':' + field[-4:]

    # query
    results = []
    dataset_mapping = {'TRAIN': train_dataset, 'ATIME': attime_dataset, 'DTIME': dtime_dataset, 'RUN-TIME': runtime_dataset}
    for table in query_tables:
        if len(table) == 0:
            continue
        table_name = table[0]
        dataset = dataset_mapping[table_name]

        result = []
        all_unmatch = True
        for row in dataset:
            row = row[1:-1].split()
            unmatch = False
            is_append = False
            for column, field in zip(row, table):
                if column != field:
                    if field[0] != '?':
                        unmatch = True
                        break
                    elif field == query_variable:
                        result.append(column)
                        is_append = True

            if unmatch and is_append:
                result.pop()
            all_unmatch = all_unmatch and unmatch

        if all_unmatch:
            return []

        if len(result) != 0:
            results.append(result)

    results = list(reduce(lambda a, b: set(a) & set(b), results))

    return results