import sys
from PyQt5 import QtWidgets

from welcome import WelcomeShow
from ui_main import UiMain


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    welcome_show = QtWidgets.QWidget()
    welcome_s_ui = WelcomeShow()
    window_s_ui = UiMain()

    welcome_s_ui.setup_ui(welcome_show, window_s_ui)
    welcome_show.show()
    sys.exit(app.exec_())