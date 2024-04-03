"""ViewColor shows the selected color"""
#  GNU GENERAL PUBLIC LICENSE v3
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from PySide6.QtGui import QColor, QPaintEvent, QPainter, QBrush
from PySide6.QtWidgets import QLineEdit
from attribox import AttriBox
from ezside.core import SolidFill, emptyPen
from ezside.widgets import BaseWidget, Vertical, VerticalSpacer
from vistutils.waitaminute import typeMsg


class ColorBox(AttriBox):
  """ColorBox provides a color box"""

  def __set__(self, instance: QColor, value: Any) -> None:
    """Set the color"""
    if isinstance(value, QColor):
      self.__get__(instance, self._getFieldOwner()).setRed(value.red())
      self.__get__(instance, self._getFieldOwner()).setGreen(value.green())
      self.__get__(instance, self._getFieldOwner()).setBlue(value.blue())
      return
    if not isinstance(value, QColor):
      e = typeMsg('value', value, QColor)
      raise TypeError(e)
    super().__set__(instance, value)


class ViewColor(BaseWidget):
  """ViewColor shows the selected color"""

  currentColor = ColorBox[QColor](127, 127, 127, 255)
  baseLayout = AttriBox[Vertical]()
  intEdit = AttriBox[QLineEdit]()
  hexEdit = AttriBox[QLineEdit]()
  spacer = AttriBox[VerticalSpacer]()

  def initUi(self) -> None:
    """Implementation of UI"""
    self.intEdit.setReadOnly(True)
    self.hexEdit.setReadOnly(True)
    self.updateLines()
    self.baseLayout.addWidget(self.intEdit)
    self.baseLayout.addWidget(self.hexEdit)
    self.setLayout(self.baseLayout)

  def asInt(self) -> tuple[int, int, int]:
    """Get the color as int"""
    return (self.currentColor.red(),
            self.currentColor.green(),
            self.currentColor.blue())

  def asHex(self) -> str:
    """Get the color as hex"""
    r, g, b = self.asInt()
    return f'#{r:02x}{g:02x}{b:02x}'

  def updateLines(self) -> None:
    """Updates the text in the lines to reflect the current color"""
    intMsg = """Current color is: (R: %d, G: %d, B: %d)""" % self.asInt()
    hexMsg = """Current color is: %s""" % self.asHex()
    self.intEdit.setText(intMsg)
    self.hexEdit.setText(hexMsg)

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paint the event"""
    BaseWidget.paintEvent(self, event)
    painter = QPainter()
    painter.begin(self)
    brush = QBrush()
    brush.setColor(self.currentColor)
    brush.setStyle(SolidFill)
    painter.setBrush(brush)
    painter.setPen(emptyPen())
    viewRect = painter.viewport()
    painter.drawRect(viewRect)
    painter.end()
