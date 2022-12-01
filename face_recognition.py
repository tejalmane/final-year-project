# import re
from sys import path
from tkinter import*
from tkinter import ttk
import face_recognition
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:
    def findEncodings (images):
        encodingList = []
        for img in images:
            img = cv2.imread(f'{path}/{img}')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converted to RGB 
            encode = face_recognition.face_encodings(img)[0]
            encodingList.append(encode)
        return encodingList
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()