from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
    QSizePolicy,
)

import image_iterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Laboratory Work №5")
        self.setMinimumSize(800, 600)
        max_width, max_height = self.center()
        self.setMaximumSize(max_width, max_height)
        self.setWindowIcon(QIcon("logo.png"))
        
        self.iterator = None
        self.current_image_path = None
        
        self.init_ui()
        
        
    def init_ui(self):    
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.image_label = QLabel("Выберите папку с датасетом", self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 3px solid black;")
        self.layout.addWidget(self.image_label, stretch=1)
        self.image_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
            
        )
        
        self.annotation_button = QPushButton("Выбрать аннотацию", self)
        self.annotation_button.clicked.connect(self.choose_annotation)
        self.layout.addWidget(self.annotation_button)
        
        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.show_next_image)
        self.layout.addWidget(self.next_button)
        
        
    def choose_annotation(self):
        file_dialog_result = QFileDialog.getOpenFileName(self, "Выбрать аннотацию", "", "CSV Files (*.csv)")
        annotation_path = file_dialog_result[0]
        if annotation_path:
            try:
                self.iterator = image_iterator.ImageIterator(annotation_path)
                self.next_button.setEnabled(True)
                self.show_next_image()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить итератор: {str(e)}")
    
    
    def show_next_image(self):
        if self.iterator:
            try:
                self.current_image_path = next(self.iterator)
                pixmap = QPixmap(self.current_image_path)
                if pixmap.isNull():
                    raise ValueError("Не удалось загрузить изображение")
                
                self.image_label.setPixmap(
                    pixmap.scaled(
                        self.image_label.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
            except StopIteration:
                QMessageBox.information(self, "Конец датасета", "Вы просмотрели все изображения в аннотации.")
                self.next_button.setEnabled(False)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при загрузке изображения: {str(e)}")
        
        
    def center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_rect = self.geometry()
        
        x = (screen_geometry.width() - window_rect.width()) // 2
        y = (screen_geometry.height() - window_rect.height()) // 2
        
        self.move(x, y)
        
        return screen_geometry.width(), screen_geometry.height()

