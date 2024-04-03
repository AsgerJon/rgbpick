"""App subclasses QApplication and is the main entry point for the
application."""
#  GNU GENERAL PUBLIC LICENSE v3
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

MenuFlag = Qt.ApplicationAttribute.AA_DontUseNativeMenuBar


class App(QApplication):
  """App is a subclass of QApplication."""

  __caller_id__ = None

  icons = None

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the App instance."""
    QApplication.__init__(self, *args, **kwargs)
    self.setApplicationName('RGB Picker')
    self.setApplicationDisplayName('RGB Picker')
    self.setAttribute(MenuFlag, True)
