"""
Provides QtNetwork classes and functions.
"""
import os
from pyqode.qt import QT_API
from pyqode.qt import PYQT5_API
from pyqode.qt import PYQT4_API
from pyqode.qt import PYSIDE_API
from pyqode.qt import PYSIDE2_API

if os.environ[QT_API] in PYQT5_API:
    from PyQt5.QtNetwork import *
    print("PYQT5_API")
elif os.environ[QT_API] in PYQT4_API:
    from PyQt4.QtNetwork import *
    print("PYQT4_API")
elif os.environ[QT_API] in PYSIDE_API:
    from PySide.QtNetwork import *
    print("PYSIDE_API")
elif os.environ[QT_API] in PYSIDE2_API:
    from PySide2.QtNetwork import *
    print("PYSIDE2_API")
else:
    raise ImportError('No Qt bindings could be found')
