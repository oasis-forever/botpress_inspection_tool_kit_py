import sys
sys.path.append("../lib/concerns")
import json
from json_exporter import gen_learning_data_list
from file_handler import write_json

class JsonConverter:
    def __init__(self):
        self.obj = None

    def csv_to_dict(self, csv_path):
        self.obj = { "qnas": gen_learning_data_list(csv_path) }
        return self.obj["qnas"]

    def dict_to_json(self, json_path):
        write_json(json_path, self.obj)
