from ui.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication
import logging


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__init()


    def __init(self):
        self.switch_pages = {
            'main': [self.page_main, self.btn_open_main],
            'settings': [self.page_settings, self.btn_open_settings],
            'records': [self.page_records, self.btn_open_records],
        }
        self.box_modes = {
            'Автоматический': self.page_automate,
            'Переодический': self.page_period,
            'Запланированный': self.page_plan,
        }
        self.box_start_mode.currentIndexChanged.connect(self.box_mode_switcher)
        self.btns_connect()

    def btns_connect(self):
        for k, v in self.switch_pages.items():
            v[1].clicked.connect(getattr(self, f"open_{k}_page"))

    def open_main_page(self):
        self.pages.setCurrentWidget(self.page_main)
        for k, v in self.switch_pages.items():
            self.set_style(v[1], 'color', '#FFFFFF')
        self.set_style(self.btn_open_main, 'color', '#29D37E')

    def open_settings_page(self):
        self.pages.setCurrentWidget(self.page_settings)
        for k, v in self.switch_pages.items():
            self.set_style(v[1], 'color', '#FFFFFF')
        self.set_style(self.btn_open_settings, 'color', '#29D37E')

    def open_records_page(self):
        self.pages.setCurrentWidget(self.page_records)
        for k, v in self.switch_pages.items():
            self.set_style(v[1], 'color', '#FFFFFF')
        self.set_style(self.btn_open_records, 'color', '#29D37E')

    def set_style(self, obj, attribute, value):
        style = obj.styleSheet()
        if style.find(attribute) != -1:
            ind1 = style.find(attribute)
            ind2 = style.find(';', ind1 + 1)
            new_style = style.replace(style[ind1:ind2], f"{attribute}: {value}")
            obj.setStyleSheet(new_style)
        else:
            obj.setStyleSheet(f"{obj.styleSheet()}\n{attribute}: {value};")

    def box_mode_switcher(self):
        selected_mode = self.box_start_mode.currentText()
        mode_page = self.box_modes[selected_mode]
        self.start_settings.setCurrentWidget(mode_page)

def start_app():
    import sys
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())