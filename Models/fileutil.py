def load_file(file_path):
    with open(file_path, 'r') as f:
        dataset = []
        for row in f.readlines():
            dataset.append(row if row[-1] != '\n' else row[:-1])
        return dataset

def save_file(lst, file_path):
    with open(file_path, 'w') as f:
        for data in lst:
            f.write(data + "\n")