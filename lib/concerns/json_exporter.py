import csv
from file_handler import uniq_list

def gen_dict_template():
    return {
      "id": "",
      "data": {
        "action": "text",
        "contexts": [
          "hoge"
        ],
        "enabled": True,
        "answers": {
          "ja": ["hoge"]
        },
        "questions": {
          "ja": []
        },
        "redirectFlow": "",
        "redirectNode": ""
      }
    }

def gen_learning_data_list(csv_path):
    learning_data = []
    dict_template = gen_dict_template()
    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for learning_datum in reader:
            if dict_template["data"]["answers"]["ja"][-1] == learning_datum[2]:
                dict_template["data"]["questions"]["ja"].append(learning_datum[1])
            else:
                dict_template = gen_dict_template()
                dict_template["id"] = learning_datum[0]
                dict_template["data"]["questions"]["ja"].append(learning_datum[1])
                dict_template["data"]["answers"]["ja"].remove("hoge")
                dict_template["data"]["answers"]["ja"].append(learning_datum[2])
            dict_template["data"]["questions"]["ja"] = uniq_list(dict_template["data"]["questions"]["ja"])
            learning_data.append(dict_template)
    return uniq_list(learning_data)
