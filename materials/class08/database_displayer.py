import sys
from PyQt5 import QtWidgets
import pandas as pd
from qt_material import apply_stylesheet


def create_table(default_info :dict) -> pd.DataFrame:
    return pd.DataFrame(default_info)

default_header = {"task_name":["a", "b"], "task_id":[1,2], "assignee":["ty", "by"], "entity_id":[111, 222]}
table = create_table(default_header)

def add_row_to_table(tar_table :pd.DataFrame, input_info :dict) -> None:
    tar_table.loc[len(tar_table)] = input_info

input_infos = [
                {"task_name":"fx01", "task_id":123, "assignee":"bbb", "entity_id":456},
                {"task_name":"fx02", "task_id":111, "assignee":"ccc", "entity_id":333},
                {"task_name":"fx03", "task_id":122, "assignee":"ddd", "entity_id":555},
            ]
for _info in input_infos:
    add_row_to_table(table, _info)

def search_in_table(tar_table :pd.DataFrame, col_name :str, input_info :str) -> pd.DataFrame:
    return tar_table.loc[tar_table[col_name] == input_info]


class MainView(QtWidgets.QMainWindow):
    def __init__(self, _parent=None):
        super(MainView, self).__init__(_parent)

        print(len(table),len(table.columns))
        self.main_db_displayer_tb = QtWidgets.QTableWidget(len(table),len(table.columns))

        self.input_le = QtWidgets.QLineEdit()
        self.show_search_res_lb = QtWidgets.QLabel()
        self.show_search_res_lb.setStyleSheet("""QLabel {
                                                color: black;             /* 텍스트 색상 */
                                                font-size: 14px;          /* 글자 크기 */
                                                font-weight: bold;        /* 글자 굵기 */
                                                background-color: white;  /* 배경색 */
                                                border: 1px solid gray;   /* 테두리 */
                                                padding: 5px;             /* 내부 여백 */
                                                border-radius: 5px;       /* 둥근 테두리 */
                                            }""")


        self.search_part_hl = QtWidgets.QHBoxLayout()
        self.search_part_hl.addWidget(self.input_le,            2)
        self.search_part_hl.addWidget(self.show_search_res_lb,  3)


        self.start_search_btn = QtWidgets.QPushButton()
        self.start_search_btn.setText("Search")
        self.start_search_btn.clicked.connect(self.search_from_db)

        self.main_vl = QtWidgets.QVBoxLayout()
        self.main_vl.addWidget(self.main_db_displayer_tb)
        self.main_vl.addLayout(self.search_part_hl)
        self.main_vl.addWidget(self.start_search_btn)

        self.main_wg = QtWidgets.QWidget()
        self.main_wg.setLayout(self.main_vl)

        self.setCentralWidget(self.main_wg)
        self.resize(500,500)

        self.set_db()



        apply_stylesheet(self, "dark_blue.xml")


    def set_db(self):
        self.main_db_displayer_tb.setHorizontalHeaderLabels(
                                    ["task_name", "task_id", "assignee", "entity_id"]
                                    )
        self.main_db_displayer_tb.verticalHeader().setVisible(False)
        for row_idx, _row in table.iterrows():
            val_name        = _row["task_name"]
            val_id          = str(_row["task_id"])
            val_assignee    = _row["assignee"]
            val_entity_id   = str(_row["entity_id"])

            self.main_db_displayer_tb.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(val_name))
            self.main_db_displayer_tb.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(val_id))
            self.main_db_displayer_tb.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(val_assignee))
            self.main_db_displayer_tb.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(val_entity_id))

    def search_from_db(self):
        input_value = self.input_le.text()

        search_res = search_in_table(table, "task_name", input_value)
        if search_res.empty == False:
            self.show_search_res_lb.setText(search_res.iloc[0]["task_name"])
        else:
            self.show_search_res_lb.setText("없어!")

        self.input_le.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    view = MainView()
    view.show()

    app.exec_()
