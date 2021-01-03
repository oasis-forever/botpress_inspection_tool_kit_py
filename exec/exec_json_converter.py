import sys
sys.path.append("../lib")
from json_converter import JsonConverter

json_converter = JsonConverter("../csv/learning_data.csv", "../json/learning_data.json")
learning_data = json_converter.csv_to_dict()
print("\n=========================================================================")
print("Loading CSV file: {}".format(json_converter.csv_path))
json_converter.dict_to_json()
print("CSV file has successfully been loaded")
print("\n=========================================================================")
print("JSON file has successfully been exported: {}".format(json_converter.json_path))
print("The number of Q&A: {}".format(len(learning_data)))
