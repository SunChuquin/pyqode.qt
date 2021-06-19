"""
Provides QtGui classes and functions.

.. warning:: All PyQt4/PySide gui classes are exposed but when you use
    PyQt5, those classes are not available. Therefore, you should treat/use
    this package as if it was ``PyQt5.QtGui`` module.
"""
import os
from pyqode.qt import QT_API
from pyqode.qt import PYSIDE2_API


if os.environ[QT_API] in PYSIDE2_API:
    from PySide2.QtXml import *
else:
    raise ImportError('No Qt bindings could be found')
