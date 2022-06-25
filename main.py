import sys

from PyQt5 import QtWidgets

from models import create_tables, connect_database
from ui_extend import LoginDialogEx, MainWindowEx

if __name__ == '__main__':
    create_tables()
    connect_database()
    app = QtWidgets.QApplication(sys.argv)
    app.addLibraryPath(".")
    login = LoginDialogEx()
    main = MainWindowEx()
    login.loginUser.connect(lambda x:main.show())
    login.show()
    sys.exit(app.exec_())