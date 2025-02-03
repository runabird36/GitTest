# Pandas definition : python Module for Database
# Database :
#           - backend
#           - the feature or structure for users to store data
#
# Two categories of Database
#   - a relational database management system   : ex - MySQL, pandas
#   - a NoSQL database system                   : ex - MongoDB
#
# api = group of functions or classes
#   ex) import pandas
#   ex) import ...
#
# CRUD for api
#   - C : Create api
#   - R : Read api
#   - U : Update api
#   - D : Delete api
# import pandas
# from pandas import DataFrame

# ===========
# Create
# ===========
import pandas as pd

def create_table(default_info :dict) -> pd.DataFrame:
    return pd.DataFrame(default_info)

default_header = {"task_name":["a", "b"], "task_id":[1,2], "assignee":["ty", "by"], "entity_id":[111, 222]}
table = create_table(default_header)
print(table)

# ===========
# Update
# ===========
def add_row_to_table(tar_table :pd.DataFrame, input_info :dict) -> None:
    tar_table.loc[len(tar_table)] = input_info


input_data = {"task_name":"c", "task_id":3, "assignee":"dh", "entity_id":333}
add_row_to_table(table, input_data)
print(table)



input_infos = [
                {"task_name":"fx01", "task_id":123, "assignee":"bbb", "entity_id":456},
                {"task_name":"fx02", "task_id":111, "assignee":"ccc", "entity_id":333},
                {"task_name":"fx03", "task_id":122, "assignee":"ddd", "entity_id":555},
            ]
for _info in input_infos:
    add_row_to_table(table, _info)

print(table)

# table.to_excel(excel_writer="C:/dev/test.xlsx", sheet_name="TY")
# table.to_json("C:/dev/test.json")
