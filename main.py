import sys

from PyQt5 import QtWidgets

from models import create_tables, connect_database
from ui_extend import LoginDialogEx

if __name__ == '__main__':
    create_tables()
    connect_database()
    app = QtWidgets.QApplication(sys.argv)
    app.addLibraryPath(".")
    login = LoginDialogEx()
    login.show()
    sys.exit(app.exec_())