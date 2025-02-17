import pandas as pd

# ===========
# Create
# ===========

def create_table(default_info :dict) -> pd.DataFrame:
    return pd.DataFrame(default_info)

default_header = {"task_name":["a", "b"], "task_id":[1,2], "assignee":["ty", "by"], "entity_id":[111, 222]}
table = create_table(default_header)


# ===========
# Update
# ===========
def add_row_to_table(tar_table :pd.DataFrame, input_info :dict) -> None:
    tar_table.loc[len(tar_table)] = input_info





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


# =======================================================
# Read one row which has keyword that user want to put
# =======================================================
def search_in_table(tar_table :pd.DataFrame, col_name :str, input_info :str) -> pd.DataFrame:
    return tar_table.loc[tar_table[col_name] == input_info]


selected_row = search_in_table(table, "task_name", "fx01")
print(selected_row)

# =======================================================
# Read one cell
# =======================================================
# print(table.iloc[0]["task_name"])




# =======================================================
# Read all row using for-loop
# =======================================================
for _idx, _row in table.iterrows():
    # print(_row)
    print(_idx, _row["task_id"])
