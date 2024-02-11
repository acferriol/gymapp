#Util functions for some tasks
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
import argparse
import os
from pathlib import Path
from reportlab.pdfgen import canvas


BASE_DIR = Path(__file__).resolve().parent.parent

def generate_card(nombre,apellido,url):
    path_root = "media/Tarjeta_"+nombre+"_"+apellido+".pdf"
    path = str(BASE_DIR / path_root)
    c = canvas.Canvas(path)
    text = c.beginText(25,25)
    text.setFont("Times-Roman",48)
    text.textLine(nombre+" "+apellido)
    c.drawText(text)
    path = generate_qrcode(url)
    c.drawImage(path,70,70)
    c.save()
    return path_root


def generate_qrcode(url):
    id = url[-1]
    path = "media/"+id+".png"
    path = BASE_DIR / path 
    img = qrcode.make(url)
    f = open(path,"wb")
    img.save(f)
    f.close()
    return path

#from utils import generate_card
#generate_card("Alejandro","Cespon","https://localhost:8000/clientes/1")