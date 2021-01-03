import os
import csv
import sys
sys.path.append("../lib/concerns")
from matrix_exporter import set_header, set_row
from api_caller import get_api_response
from file_handler import csv_to_list_with_index

class ConverseApi:
    def __init__(self, protocol, host, bot_id, user_id):
        self.url = "{}://{}/api/v1/bots/{}/converse/{}/secured?include=state,suggestions".format(protocol, host, bot_id, user_id)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": os.environ["BOTPRESS_BEARER"]
        }

    def export_csv(self, matrix_chart, test_data):
        with open(matrix_chart, "w") as w:
            writer = csv.writer(w)
            writer.writerow(set_header(csv_to_list_with_index(test_data, 0)))
            with open(test_data) as r:
                reader = csv.reader(r)
                next(reader)
                answers_list = csv_to_list_with_index(test_data, 2)
                for test_datum in reader:
                    writer.writerow(set_row(test_datum, answers_list, get_api_response(test_datum[1], self.url, self.headers).read()))
