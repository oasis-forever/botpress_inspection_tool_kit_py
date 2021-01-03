import sys
sys.path.append("../lib/concerns")
import json
from json_exporter import gen_learning_data_list
from file_handler import write_json

class JsonConverter:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def csv_to_dict(self):
        self.obj = { "qnas": gen_learning_data_list(self.csv_path) }
        return self.obj["qnas"]

    def dict_to_json(self):
        write_json(self.json_path, self.obj)
