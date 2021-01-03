import unittest
import json
import csv
import os.path
from os import path
import sys
sys.path.append("../lib")
sys.path.append("../lib/concerns")
from json_converter import JsonConverter
from file_handler import csv_to_list_with_index, uniq_list

class TestJsonConverter(unittest.TestCase):
    def setUp(self):
        self.csv_path       = "../csv/learning_data.csv"
        self.json_path      = "../json/learning_data.json"
        self.json_converter = JsonConverter(self.csv_path, self.json_path)
        self.learning_data  = self.json_converter.csv_to_dict()
        self.first_qna      = self.learning_data[0]
        self.first_qna      = self.json_converter.csv_to_dict()[0]

    def test_number_of_learning_data(self):
        self.assertEqual(len(uniq_list(csv_to_list_with_index(self.csv_path, 0))), len(self.learning_data))

    def test_qa_num(self):
        self.assertEqual("QA001", self.first_qna["id"])

    def test_questions(self):
        self.assertEqual("GitHubとは何ですか", self.first_qna["data"]["questions"]["ja"][0])
        self.assertEqual("GitHubとはどんなシステムか", self.first_qna["data"]["questions"]["ja"][1])
        self.assertEqual("GitHubって何", self.first_qna["data"]["questions"]["ja"][2])
        self.assertEqual("GitHubってなに", self.first_qna["data"]["questions"]["ja"][3])

    def test_answers(self):
        self.assertEqual("ソフトウェア開発のプラットフォームであり、ソースコードをホスティングする。コードのバージョン管理システムにはGitを使用します。", self.first_qna["data"]["answers"]["ja"][0])

    def test_json_presence(self):
        self.json_converter.dict_to_json()
        self.assertEqual(True, path.exists(self.json_path))

if __name__ == "__main__":
    unittest.main()
