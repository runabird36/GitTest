from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QComboBox,QPushButton
import sys

class TreeWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # QTreeWidget 생성
        self.tree = QTreeWidget(self)
        self.tree.setHeaderLabels(["Name", "Description"])  # 헤더 설정
        self.setCentralWidget(self.tree)

        self.tree.setItemsExpandable(False)

        # 루트 항목 생성
        root_item = QTreeWidgetItem(self.tree)
        root_item.setText(0, "Root Item01")
        combo1 = QComboBox()
        combo1.addItems(["1","2","3"])
        self.tree.setItemWidget(root_item, 1, combo1)


        root_item02 = QTreeWidgetItem(root_item)
        root_item02.setText(0, "Child Item01")
        combo2 = QComboBox()
        combo2.addItems(["4","5","6"])
        self.tree.setItemWidget(root_item02, 1, combo2)

        # 루트 항목 생성
        root_item03 = QTreeWidgetItem(self.tree)
        root_item03.setText(0, "Root Item02")
        combo1 = QComboBox()
        combo1.addItems(["1","2","3"])
        self.tree.setItemWidget(root_item03, 1, combo1)

        root_item04 = QTreeWidgetItem(root_item03)
        root_item04.setText(0, "Child Item02")
        combo2 = QComboBox()
        combo2.addItems(["4","5","6"])
        self.tree.setItemWidget(root_item04, 1, combo2)

        self.tree.collapseAll()

        # # 자식 항목 생성
        # child_item1 = QTreeWidgetItem(root_item)
        # child_item1.setText(0, "Child 1")
        # child_item1.setText(1, "This is the first child")

        # child_item2 = QTreeWidgetItem(root_item)
        # child_item2.setText(0, "Child 2")
        # child_item2.setText(1, "This is the second child")

        # # 더 많은 자식 항목을 추가하거나 계층을 확장할 수 있습니다.
        # root_item.addChild(child_item1)
        # root_item.addChild(child_item2)

        # 트리 전체 펼치기
        self.tree.expandAll()

        # 윈도우 설정
        self.setWindowTitle("QTreeWidget Example")
        self.setGeometry(300, 300, 400, 300)

        # 4 row 0 column 데이터 가져오기기
        tar_item = self.tree.topLevelItem(1)
        child_item = tar_item.child(0)
        print(child_item.text(0))





# 애플리케이션 실행
app = QApplication(sys.argv)
window = TreeWidgetExample()
window.show()
sys.exit(app.exec_())
