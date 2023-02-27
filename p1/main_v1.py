#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:40:24 2023

@author: fernando
"""

import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QDesktopWidget,QApplication, QMainWindow, QWidget,QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDateEdit,QAction,QMenuBar
from PyQt5.QtCore import QDate

class MainWindow(QMainWindow):
    
    clicksBotton = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web scraping a tarifaluzhora.es")
        self.resize(600,400)
        #self.move(600,300)
        #self.setGeometry(0, 0, 600, 400)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        self.init_ui()


    def init_ui(self):
        

        ## Widgets
        
        self.label = QLabel('¡Hola, mundo!', self)
        self.label.setGeometry(100, 50, 200, 50)
        

        
        self.labelClick = QLabel( self)
        self.labelClick.setGeometry(100, 70, 300, 60)
        
        ## Prueba de evento simple
        
        self.button = QPushButton('Haz clic aquí', self)
        self.button.setGeometry(100, 110, 100, 30)
        self.button.clicked.connect(self.buttonClicked)

        '''
        # Selección de la fecha
        self.date_label = QLabel("Selecciona la fecha: ", self)
        self.date_label.setGeometry(100, 200, 200, 50)
        #self.date_label.move(100,200)

        self.date_edit = QDateEdit(self)
        self.date_edit.move(100,240)
        self.date_edit.setCalendarPopup(True)
        
        d = QDate(2023, 2, 20)
        self.date_edit.setDate(d)

      # Salida para la función de calcula precio

        self.price_label = QLabel("Precio de la luz: ", self)
        self.price_label.setGeometry(10, 320, 300, 40)
        #self.price_label.move(100,320)


        ## Llamada a la consulta del precio de la luz
        self.scraping_button = QPushButton("Hacer web scraping", self)
        self.scraping_button.setGeometry(100, 280, 100, 30)
        #self.scraping_button.move(100,280)
        self.scraping_button.clicked.connect(self.do_scraping)
        '''

    def buttonClicked(self):
        self.clicksBotton += 1

        self.labelClick.setText(f'¡Has hecho clic en el botón {self.clicksBotton} veces')
        


    def do_scraping(self):
        
        # Obtenemos la fecha de la entrada data_edit
        selected_date = self.date_edit.date().toString("dd/MM/yyyy")

        # Hacemos el request a la web tarifaluzhora.es

        url = f"https://tarifaluzhora.es/?tarifa=pcb&fecha={selected_date}"

        response = requests.get(url)
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        resultsDia = soup.find(id="price_summary")
        # Find the element with the price of the electricity
        resultsPrecioInstantaneo = resultsDia.find("div", class_="gauge_day")

        price_text = resultsPrecioInstantaneo.text.strip()
        # Update the label with the price
        self.price_label.setText(f"Precio medio de la luz: {price_text}")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
