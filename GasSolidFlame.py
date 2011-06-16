#!/usr/bin/python -tt
import sys

from PySide import QtCore, QtGui
from core import GSController

def main():
  app = QtGui.QApplication(sys.argv)
  cont = GSController.GSController()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()



  