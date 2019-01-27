#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    ZetCode PyQt5 tutorial
    
    In this example, we dispay an image
    on the window.
    
    Author: Jan Bodnar
    Website: zetcode.com
    Last edited: August 2017
    """

from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication,QPushButton)
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import pyqtSlot
import os

class DataClassifier(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    
    def initUI(self):
        
        self.hbox = QHBoxLayout(self)
        self.imageCounter=0
        self.images=[]
        self.buttonPlace=10
        self.buttonGap=100
        self.lbl = QLabel(self)
        self.getImages()
        print(self.images)
        self.displayImage()
        
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        
        self.move(300, 200)
        self.placeButtons()
        self.setWindowTitle('Image Labelling')
        self.show()
    
    def displayImage(self):
        pixmap = QPixmap("./imagesToSort/"+self.images[self.imageCounter])
        self.lbl.setPixmap(pixmap)
        self.update()
    
    def placeButtons(self):
        button_intro = QPushButton('Introvert', self)
        button_intro.move(10,5)
        button_intro.clicked.connect(self.on_click_intro)
        
        button_extro = QPushButton('Extrovert', self)
        button_extro.move(110,5)
        button_extro.clicked.connect(self.on_click_extro)
    
        button_intu = QPushButton('Intuitive', self)
        button_intu.move(210,5)
        button_intu.clicked.connect(self.on_click_intu)
    
        button_obser = QPushButton('Observant', self)
        button_obser.move(310,5)
        button_obser.clicked.connect(self.on_click_obser)
        
        button_feel = QPushButton('Feeling', self)
        button_feel.move(410,5)
        button_feel.clicked.connect(self.on_click_feel)
                
        button_think = QPushButton('Thinking', self)
        button_think.move(510,5)
        button_think.clicked.connect(self.on_click_think)

        button_jud = QPushButton('Judging', self)
        button_jud.move(10,25)
        button_jud.clicked.connect(self.on_click_jud)
    
        button_pro = QPushButton('Prospecting', self)
        button_pro.move(110,25)
        button_pro.clicked.connect(self.on_click_pro)
        
        button_asser = QPushButton('Assertive', self)
        button_asser.move(210,25)
        button_asser.clicked.connect(self.on_click_asser)
    
        button_turbo = QPushButton('Turbulent', self)
        button_turbo.move(310,25)
        button_turbo.clicked.connect(self.on_click_turbo)
    
    
    @pyqtSlot()
    def on_click_intro(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Mind/Introvert/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_extro(self):
#        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Mind/Extrovert/"+)
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Mind/Extrovert/"+self.images[self.imageCounter])
        self.nextImage()

    def on_click_intu(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Energy/Intuitive/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_obser(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Energy/Observant/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_feel(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Nature/Feeling/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_think(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Nature/Thinking/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_jud(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Tactics/Judging/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_pro(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Tactics/Prospecting/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_asser(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Identity/Assertive/"+self.images[self.imageCounter])
        self.nextImage()
    
    def on_click_turbo(self):
        os.rename("./imagesToSort/"+self.images[self.imageCounter], "./Identity/Turbulent/"+self.images[self.imageCounter])
        self.nextImage()
    
    
    def nextImage(self):
        if(len(self.images)!=self.imageCounter):
            self.imageCounter+=1
            self.displayImage()
            print(self.imageCounter)
            print(self.images[self.imageCounter])

    def getImages(self):
        directory = os.fsencode("./imagesToSort/")
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg") or filename.endswith(".png"):
                self.images.append(filename)
                continue
            else:
                continue
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = DataClassifier()
    sys.exit(app.exec_())



