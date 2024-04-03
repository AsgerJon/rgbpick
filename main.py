"""Main Tester Script"""
#  GNU GENERAL PUBLIC LICENSE v3
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from icecream import ic

from rgbpick import MainWindow, App


def tester00() -> None:
  """LMAO"""
  stuff = ['Hello World!', os, sys, ic, ]
  for item in stuff:
    ic(item)


def tester01() -> None:
  """LMAO"""
  app = App(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())


if __name__ == '__main__':
  tester01()
