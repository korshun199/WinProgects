import sys
import serial.tools.list_ports
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загружаем твой визуальный шедевр
        loader = QUiLoader()
        ui_file = QFile("ui/main.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        # Находим твои кнопки по именам из Designer
        self.ui.btn_start.clicked.connect(self.scan_ports)
        
        # Сразу показываем окно
        self.setCentralWidget(self.ui)
        self.setWindowTitle("Масин пульт управления")

    def scan_ports(self):
        # Логика для твоих USB COM портов
        ports = serial.tools.list_ports.comports()
        self.ui.port_list.clear()
        for port in ports:
            self.ui.port_list.addItem(port.device)
        print("Олежка, я просканировала все твои дырочки... то есть порты!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())