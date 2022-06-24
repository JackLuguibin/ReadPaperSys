# 登录界面
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox

from models import User
from ui import Ui_LoginDialog


class LoginDialogEx(QDialog, Ui_LoginDialog):
    loginUser = pyqtSignal(dict)
    loginAdmin = pyqtSignal()

    def __init__(self):
        super(LoginDialogEx, self).__init__()
        self.setupUi(self)
        self.initLabel()

        self.initButton()

        self.showLogin()

        self.resize(600, 400)
        self.setFixedSize(self.width(), self.height())

    def showLogin(self, account="", psw=""):
        self.w_login.show()
        self.w_forget.hide()
        self.w_register.hide()
        self.setWindowTitle("登录")
        self.le_login_account.setText(account)
        self.le_login_psw.setText(psw)

    def showRegister(self):
        self.w_login.hide()
        self.w_forget.hide()
        self.w_register.show()
        self.setWindowTitle("注册")
        self.le_forget_account.clear()
        self.le_forget_psw.clear()
        self.le_forget_psw_again.clear()

    def showForget(self):
        self.w_login.hide()
        self.w_forget.show()
        self.w_register.hide()
        self.setWindowTitle("忘记密码")
        self.lb_register_account.clear()
        self.lb_register_name.clear()
        self.lb_register_psw.clear()
        self.lb_register_psw_again.clear()
        self.rb_man.setChecked(True)
        self.rb_woman.setChecked(False)

    def initButton(self):
        def click_pb_login():
            account = self.le_login_account.text()
            psw = self.le_login_psw.text()
            if not account:
                QMessageBox.warning(self, "登录错误", "手机号为空！", QMessageBox.Yes)
                return
            if not psw:
                QMessageBox.warning(self, "登录错误", "密码为空！", QMessageBox.Yes)
                return

            user = User.get_or_none(User.account == account)

            if not user:
                QMessageBox.warning(self, "登录错误", "用户不存在！", QMessageBox.Yes)
                return
            if user.password != psw:
                QMessageBox.warning(self, "登录错误", "用户密码错误！", QMessageBox.Yes)
                return
            print("send")
            self.loginUser.emit({
                "account": account,
                "uuid": user.uuid,
                "name": user.name,
                "identity": user.identity
            })
            self.close()

        self.pb_login.clicked.connect(click_pb_login)

        def click_pb_admin_login():
            account = self.le_login_account.text()
            psw = self.le_login_psw.text()
            if not account:
                QMessageBox.warning(self, "登录错误", "手机号为空！", QMessageBox.Yes)
                return
            if not psw:
                QMessageBox.warning(self, "登录错误", "密码为空！", QMessageBox.Yes)
                return

            user = User.get_or_none(User.account == account)

            if not user:
                QMessageBox.warning(self, "登录错误", "用户不存在！", QMessageBox.Yes)
                return
            if user.password != psw:
                QMessageBox.warning(self, "登录错误", "用户密码错误！", QMessageBox.Yes)
                return
            if user.identity != User.COMMON:
                self.loginAdmin.emit()
                self.close()
            else:
                QMessageBox.warning(self, "登录错误", "非管理员账号！", QMessageBox.Yes)
                return

        self.pb_admin_login.clicked.connect(click_pb_admin_login)

        def click_pb_register(identity):
            try:
                account = self.lb_register_account.text()
                name = self.lb_register_name.text()
                age = self.le_age.text()
                psw = self.lb_register_psw.text()
                psw_again = self.lb_register_psw_again.text()
                sex = True if self.rb_man.isChecked() else False
                if not account:
                    QMessageBox.warning(self, "注册错误", "手机号为空！", QMessageBox.Yes)
                    return
                if not name:
                    QMessageBox.warning(self, "注册错误", "姓名为空！", QMessageBox.Yes)
                    return
                if not age:
                    QMessageBox.warning(self, "注册错误", "年龄为空！", QMessageBox.Yes)
                    return
                if not psw and not psw_again:
                    QMessageBox.warning(self, "注册错误", "密码为空！", QMessageBox.Yes)
                    return
                if psw != psw_again:
                    QMessageBox.warning(self, "注册错误", "密码不一致！", QMessageBox.Yes)
                    return

                user = User.get_or_none(User.account == account)

                if user:
                    QMessageBox.warning(self, "注册错误", "用户已存在！", QMessageBox.Yes)
                    return
                else:
                    try:
                        user = User.create(
                            account=account,
                            password=psw,
                            name=name,
                            age=int(age) if age else 0,
                            sex=sex,
                            identity=identity
                        )
                        user.save()
                    except Exception as e:
                        print(e)
                QMessageBox.information(self, "注册", "注册成功！")
                self.showLogin(account, psw)
            except Exception as e:
                print(e)

        self.pb_register.clicked.connect(lambda: click_pb_register(User.COMMON))
        self.pb_register_work.clicked.connect(lambda: click_pb_register(User.WORK))

        def click_pb_modify():
            account = self.le_forget_account.text()
            psw = self.le_forget_psw.text()
            psw_again = self.le_forget_psw_again.text()
            if not account:
                QMessageBox.warning(self, "忘记密码错误", "手机号为空！", QMessageBox.Yes)
                return

            if psw != psw_again:
                QMessageBox.warning(self, "注册错误", "密码不一致！", QMessageBox.Yes)
                return

            user = list(User.select().filter(User.account == account))
            print(user)
            if not user:
                QMessageBox.warning(self, "注册错误", "用户不存在！", QMessageBox.Yes)
                return
            user[0].password = psw
            user[0].save()
            QMessageBox.warning(self, "修改密码", "修改成功！", QMessageBox.Yes)
            self.showLogin(account, psw)

        self.pb_modify.clicked.connect(click_pb_modify)

    def initLabel(self):
        self.lb_register.linkActivated.connect(self.showRegister)
        self.lb_forget.linkActivated.connect(self.showForget)
        self.lb_login.linkActivated.connect(self.showLogin)
        self.lb_login_2.linkActivated.connect(self.showLogin)
