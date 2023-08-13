```python
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.backend.webscraper_integration import integrate_webscraper

class CheckboxHandler(QWidget):
    def __init__(self):
        super().__init__()

        self.webscraper_checkbox = QCheckBox("Enable Web Scraper", self)
        self.webscraper_checkbox.stateChanged.connect(self.handle_checkbox)

        layout = QVBoxLayout()
        layout.addWidget(self.webscraper_checkbox)

        self.setLayout(layout)

    def handle_checkbox(self, state):
        if state == Qt.Checked:
            print("Checkbox Clicked")
            integrate_webscraper(True)
        else:
            integrate_webscraper(False)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    checkbox_handler = CheckboxHandler()
    checkbox_handler.show()

    sys.exit(app.exec_())
```