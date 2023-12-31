import os
import sys

from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

sys.path.insert(0, "C:\Users\G604088\OneDrive - Sagemcom Broadband SAS\Documents\7 - Calibration\7-CalibGui\GUI_proto\pyqt5_qtquick2_example")
import resources.py  # load resources built by pyrcc5


# Set the QtQuick Style
# Acceptable values: Default, Fusion, Imagine, Material, Universal.
os.environ['QT_QUICK_CONTROLS_STYLE'] = (sys.argv[1]
                                         if len(sys.argv) > 1 else "Default")

# Create an instance of the application
# QApplication MUST be declared in global scope to avoid segmentation fault
app = QApplication(sys.argv)

# Create QML engine
engine = QQmlApplicationEngine()

# Load the qml file into the engine
engine.load(QUrl('qrc:/pyqt5_qtquick2_example/qml/main.qml'))

# Qml file error handling
if not engine.rootObjects():
    sys.exit(-1)

# Send QT_QUICK_CONTROLS_STYLE to main qml (only for demonstration)
# For more details and other methods to communicate between Qml and Python:
#   http://doc.qt.io/archives/qt-4.8/qtbinding.html
qtquick2Themes = engine.rootObjects()[0].findChild(
    QObject,
    'qtquick2Themes'
)
qtquick2Themes.setProperty('text', os.environ['QT_QUICK_CONTROLS_STYLE'])

# engine.quit.connect(app.quit)
# Unnecessary,
# since QQmlEngine.quit has already connect to QCoreApplication.quit

sys.exit(app.exec_())