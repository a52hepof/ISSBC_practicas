#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 00:09:19 2023

@author: fernando
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creamos el area de edición de texto
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Creamos el menú de opciones
        self.createMenu()

        # Configuramos la ventana principal
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Editor de Textos')

    def createMenu(self):
        # Creamos el menú
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('Archivo')

        # Creamos las acciones del menú
        openFile = QAction('Abrir', self)
        openFile.triggered.connect(self.openFileDialog)
        saveFile = QAction('Guardar', self)
        saveFile.triggered.connect(self.saveFile)
        saveFileAs = QAction('Guardar como...', self)
        saveFileAs.triggered.connect(self.saveFileAs)

        # Añadimos las acciones al menú
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveFileAs)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Abrir archivo", "","Archivos de Texto (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        if self.filePath is None:
            self.saveFileAs()
        else:
            with open(self.filePath, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def saveFileAs(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Guardar archivo como...", "","Archivos de Texto (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())
            self.filePath = fileName


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec_())