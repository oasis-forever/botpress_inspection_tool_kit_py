import csv

def write_json(path, dic):
    with open(path, "w") as f:
        f.write(json.dumps(dic, ensure_ascii=False, indent=4))

def uniq_list(duplicate_data):
    uniq_data = []
    for datum in duplicate_data:
        if not datum in uniq_data:
            uniq_data.append(datum)
    return uniq_data

