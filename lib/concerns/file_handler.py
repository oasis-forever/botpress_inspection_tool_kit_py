import json
import csv

def write_json(path, dic):
    with open(path, "w") as f:
        f.write(json.dumps(dic, ensure_ascii=False, indent=4))

def data_list(iterable_data):
    data = []
    for datum in iterable_data:
        data.append(datum)
    return data

def uniq_list(duplicate_data):
    uniq_data = []
    for datum in duplicate_data:
        if not datum in uniq_data:
            uniq_data.append(datum)
    return uniq_data

def csv_to_list_with_index(csv_file, index):
    data = []
    with open(csv_file) as f:
        reader = csv.reader(f)
        next(reader)
        for datum in reader:
            data.append(datum[index])
    return data
