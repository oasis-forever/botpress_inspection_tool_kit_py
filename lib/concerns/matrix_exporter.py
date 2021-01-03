import csv
import json
from file_handler import data_list

def set_header(serial_nums):
    header = ["Serial_Nums", "Test_Data"]
    serial_nums_list = data_list(serial_nums)
    header.extend(serial_nums_list)
    return header

def set_answers_confidence(res_body):
    res_dict = json.loads(res_body)
    answers_confidence = []
    for i in range(len(res_dict["suggestions"])):
        answers_confidence.append(
            {
                "text": res_dict["suggestions"][i]["payloads"][1]["text"],
                "confidence": res_dict["suggestions"][i]["confidence"]
            }
        )
    return answers_confidence

def set_row(test_datum, answers_list, res_body):
    row = [test_datum[0], test_datum[1]]
    confidence = ["0.0%" * 1 for i in range(len(answers_list))]
    for ans_conf in set_answers_confidence(res_body):
        index = answers_list.index(ans_conf["text"])
        confidence[index] = "{:.1f}%".format(ans_conf["confidence"] * 100)
    row.extend(confidence)
    return row
