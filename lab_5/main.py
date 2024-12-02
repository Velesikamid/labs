import sys

import main_window


def main():
    app = main_window.QApplication(sys.argv)

    window = main_window.MainWindow()
    window.show()

    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    main()
