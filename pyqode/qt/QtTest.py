"""
Provides QtTest and functions

.. warning:: PySide is not supported here, that's why there is not unit tests
    running with PySide.

"""
import os
from pyqode.qt import QT_API
from pyqode.qt import PYQT5_API
from pyqode.qt import PYQT4_API
from pyqode.qt import PYSIDE_API
from pyqode.qt import PYSIDE2_API

if os.environ[QT_API] in PYQT5_API:
    from PyQt5.QtTest import QTest
    print("PYQT5_API")
elif os.environ[QT_API] in PYQT4_API:
    print("PYQT4_API")
    from PyQt4.QtTest import QTest as OldQTest

    class QTest(OldQTest):
        @staticmethod
        def qWaitForWindowActive(QWidget):
            OldQTest.qWaitForWindowShown(QWidget)
elif os.environ[QT_API] in PYSIDE_API:
    raise ImportError('QtTest support is incomplete for PySide')
elif os.environ[QT_API] in PYSIDE2_API:
    from PySide2.QtTest import QTest
    import time
    QTest.qWait = time.sleep
    print("PYSIDE2_API")
else:
    raise ImportError('No Qt bindings could be found')
