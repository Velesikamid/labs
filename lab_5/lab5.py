import sys

import main_window


def main() -> None:
    """
    The entry point of the application.

    Creates a QApplication instance, initializes the main window,
    and starts the event loop.
    """
    app = main_window.QApplication(sys.argv)

    window = main_window.MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
