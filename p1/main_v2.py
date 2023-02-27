#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:40:24 2023

@author: fernando
"""

import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDateEdit,QAction,QMenuBar
from PyQt5.QtCore import QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web scraping a tarifaluzhora.es")
        #self.resize(600,400)
        #self.move(600,300)
        self.setGeometry(600, 300, 600, 400)

        #self.central_widget = QWidget()
        #self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('¡Hola, mundo!', self)
        self.label.setGeometry(100, 50, 200, 50)
        
        self.labelClick = QLabel( self)
        self.labelClick.setGeometry(100, 70, 200, 60)

        
        self.button = QPushButton('Haz clic aquí', self)
        self.button.setGeometry(100, 110, 100, 30)
        self.button.clicked.connect(self.buttonClicked)

        
        # Layouts
        #main_layout = QVBoxLayout()
        #date_layout = QHBoxLayout()
        #button_layout = QHBoxLayout()

        # Widgets
        self.date_label = QLabel("Selecciona la fecha: ", self)
        self.date_label.setGeometry(100, 200, 200, 50)
        #self.date_label.move(100,200)


        self.date_edit = QDateEdit(self)
        self.date_edit.move(100,240)
        self.date_edit.setCalendarPopup(True)
        
        # date
        d = QDate(2023, 2, 20)
        self.date_edit.setDate(d)

      # setting date to the date edit

        self.price_label = QLabel("Precio de la luz: ", self)
        self.price_label.setGeometry(10, 320, 300, 40)
        #self.price_label.move(100,320)



        self.scraping_button = QPushButton("Hacer web scraping", self)
        self.scraping_button.setGeometry(100, 280, 100, 30)
        #self.scraping_button.move(100,280)

        self.scraping_button.clicked.connect(self.do_scraping)



        # Add widgets to layouts
        #date_layout.addWidget(date_label)
        #date_layout.addWidget(self.date_edit)

        #button_layout.addWidget(self.scraping_button)

        #main_layout.addLayout(date_layout)
        #main_layout.addLayout(button_layout)
        #main_layout.addWidget(self.price_label)
        
        
         # Create the menu bar
        menu_bar = QMenuBar(self)
        
        # File menu
        file_menu = menu_bar.addMenu("Archivo")
        exit_action = QAction("Salir", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Set the menu bar
        self.setMenuBar(menu_bar)

        # Set the main layout for the central widget
        #self.central_widget.setLayout(main_layout)

        # Connect the button to the scraping function
        

    def buttonClicked(self):
        self.labelClick.setText('¡Has hecho clic en el botón!')




    def do_scraping(self):
        # Get the selected date from the QDateEdit widget
        selected_date = self.date_edit.date().toString("dd/MM/yyyy")

        # Make the request to the website
        #url = f"https://tarifaluzhora.es/{selected_date}"
        url = f"https://tarifaluzhora.es/?tarifa=pcb&fecha={selected_date}"

        response = requests.get(url)
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        resultsDia = soup.find(id="price_summary")
        # Find the element with the price of the electricity
        resultsPrecioInstantaneo = resultsDia.find("div", class_="gauge_day")

        price_text = resultsPrecioInstantaneo.text.strip()
        print(price_text)
        # Update the label with the price
        self.price_label.setText(f"Precio medio de la luz: {price_text}")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
