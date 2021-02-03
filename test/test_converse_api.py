import unittest
import json
import csv
import datetime
import sys
sys.path.append("../lib")
sys.path.append("../lib/concerns")
from converse_api import ConverseApi
from api_caller import get_api_response
from file_handler import csv_to_list_with_index

class TestConverseApi(unittest.TestCase):
    def setUp(self):
        protocol          = "https"
        host              = "oasist-botpress-server.herokuapp.com"
        bot_id            = "sample-bot-1"
        user_id           = "oasist"
        self.converse_api = ConverseApi(protocol, host, bot_id, user_id)
        self.res          = get_api_response("GitHubとは", self.converse_api.url, self.converse_api.headers)

    def test_status_code(self):
        self.assertEqual(200, self.res.getcode())

    def test_has_state_key(self):
        self.assertEqual(True, "state" in json.loads(self.res.read()).keys())

    def test_has_suggestions_key(self):
        self.assertEqual(True, "suggestions" in json.loads(self.res.read()).keys())

    def test_export_csv(self):
        self.assertEqual(True, "state" in json.loads(self.res.read()).keys())

    def test_export_csv(self):
        matrix_chart  = "../csv/matrix_chart_{0:%Y%m%d}.csv".format(datetime.datetime.now())
        test_data     = "../csv/test_data.csv"
        self.converse_api.export_csv(matrix_chart, test_data)
        test_rows_num   = len(csv_to_list_with_index(test_data, 0))
        matrix_rows_num = len(csv_to_list_with_index(matrix_chart, 0))
        self.assertEqual(test_rows_num, matrix_rows_num)

if __name__ == "__main__":
    unittest.main()
