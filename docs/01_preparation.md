## 1. Preparation

### 1-1. JSON File for Import

Create learning data CSV file to import Q&As all at once on Botpress.

* Place headers `Serial_Nums`, `Questions` and `Answers`
* Remove HTML tags and quotes to avoid an error raised by CSV library of Python
* Duplicate `Serial_Nums` and `Answers`(`Serial_Nums & Answers`: `Questions` = 1:N ).
* For the details, check the [Sample](https://github.com/oasis-forever/botpress_inspection_tool_kit_py/blob/master/csv/learning_data.csv)

### 1-2. Test Data

Create test data CSV file.

* Place headers `Serial_Nums`, `Questions` and `Answers`
* `Serial_Nums` : `Questions` : `Answers` : = 1:1:1
* For the details, check the [Sample](https://github.com/oasis-forever/botpress_inspection_tool_kit_py/blob/master/csv/test_data.csv)
