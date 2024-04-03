"""MainWindow provides the main application window"""
#  GNU GENERAL PUBLIC LICENSE v3
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QColorDialog, QPushButton
from attribox import AttriBox
from ezside import BaseWindow
from ezside.moreutils import EmptyField
from ezside.widgets import BaseWidget, Vertical, TextLabel, VerticalSpacer
from vistutils.waitaminute import typeMsg

from rgbpick import ViewColor


class MainWindow(BaseWindow):
  """MainWindow provides the main application window"""

  __color_dialog__ = None

  baseLayout = AttriBox[Vertical]()
  baseWidget = AttriBox[BaseWidget]()
  welcomeBanner = AttriBox[TextLabel]()
  viewColor = AttriBox[ViewColor]()
  button = AttriBox[QPushButton]()
  spacer = AttriBox[VerticalSpacer]()
  colorDialog = EmptyField()

  colorSelected = Signal(QColor)

  def createColorDialog(self, ) -> None:
    """Create a color dialog"""
    self.__color_dialog__ = QColorDialog()
    self.__color_dialog__.colorSelected.connect(self.colorSelected)

  @colorDialog.GET
  def getColorDialog(self, **kwargs) -> QColorDialog:
    """Get the color dialog"""
    if self.__color_dialog__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self.createColorDialog()
      return self.getColorDialog(_recursion=True)
    if isinstance(self.__color_dialog__, QColorDialog):
      return self.__color_dialog__
    e = typeMsg('__color_dialog__', self.__color_dialog__, QColorDialog)
    raise TypeError(e)

  def initActions(self) -> None:
    """Implementation of actions"""
    self.mainMenuBar.files.new.triggered.connect(self.newFunc)
    self.colorSelected.connect(self.applyColor)
    self.button.clicked.connect(self.newFunc)

  def initUi(self) -> None:
    """Implementation of UI"""
    self.setMinimumSize(QSize(320, 144))
    self.button.setText('Click to select color!')
    self.welcomeBanner.setText('Welcome to the RGB Picker')
    self.baseLayout.addWidget(self.welcomeBanner)
    self.baseLayout.addWidget(self.viewColor)
    self.baseLayout.addWidget(self.button)
    self.baseLayout.addWidget(self.spacer)
    self.baseWidget.setLayout(self.baseLayout)
    self.setCentralWidget(self.baseWidget)

  def newFunc(self, ) -> None:
    """New function"""
    if isinstance(self.colorDialog, QColorDialog):
      self.colorDialog.open()

  def applyColor(self, color: QColor) -> None:
    """Apply the color"""
    self.viewColor.currentColor = color
    self.viewColor.updateLines()
    self.viewColor.update()
