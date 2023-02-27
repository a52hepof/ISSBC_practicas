#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:20:57 2023

@author: fernando
"""

import sys

sys.path.append("..")

print(sys.path)
#from eventos import funcionEvento
from eventos.eventControl import funcionEvento

funcionEvento()
from PyQt5.QtWidgets import QApplication, QWidget

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 400)
    w.move(200, 0)
    w.setWindowTitle('my Firs Window : Hello pyqt5')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    






