import csv
import datetime
import sys
sys.path.append("../lib")
from converse_api import ConverseApi

protocol      = "https"
host          = "oasist-botpress-server.herokuapp.com"
bot_id        = "sample-bot-1"
user_id       = "oasist"
matrix_chart  = "../csv/matrix_chart_{0:%Y%m%d}.csv"
test_data     = "../csv/test_data.csv"
datetime      = datetime.datetime.now()

converse_api = ConverseApi(protocol, host, bot_id, user_id)
print("\n=========================================================================")
print("\nExporting Matrix CSV file...")
converse_api.export_csv(matrix_chart.format(datetime), test_data, learning_data)
print("\n=========================================================================")
print("\nMatrix CSV file has successfully been exported: '{}'".format(matrix_chart.format(datetime)))
