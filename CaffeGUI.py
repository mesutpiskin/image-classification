# -*- coding: utf-8 -*-
#######################################
__file__    = "CaffeGUI.py"
__author__  = "Mesut Piþkin"
__license__ = "GPL"
__version__ = "1.0"
__email__   = "mesutpiskin@outlook.com"
__website__ = "www.mesutpiskin.com"
__status__  = "Development"
__date__    = "21.01.2017"
#######################################
from Tkinter import *
import PIL.Image
import PIL.ImageTk
import tkFileDialog 
import CaffeClassification

#Form
frame = Tk()
frame.resizable(width=FALSE, height=FALSE) #Form boyutlandýrma yok
frame.title("Caffe ile Siniflandirma - Caffe Classification") #Form baþlýðý
frame.geometry("700x500") # Sabit form boyutlarý

#Call caffe init function - Að hazýr hale getirilmesi için inþa fonksiyonu çaðrýlýr.
CaffeClassification.InitCaffe()

#Properties
global lblImage

#Events
def OpenFile():
	#Tkinter dosya seçme bileþeni
	filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Resim Dosyasýný Seçiniz")
	imageTag =  CaffeClassification.RecognizeObject(filename) #Secilen goruntuyu parametre olarak gonderir. 
	lblTag["text"] = imageTag #Tanýmlanan görüntü label'a atanýr.
    #Selected Image File -(Secilen resim dosyasi form uzerinde goruntulenir.)
	im = PIL.Image.open(filename) #Seçilen görüntü dosyasý
	im=im.resize((700, 400)) #Resmi forma sýðmasý için boyutlandýr
	photo = PIL.ImageTk.PhotoImage(im)
	lblImage.configure(image = photo)
	lblImage.image = photo

#Form Components -(Form uzerindeki bileþenler)
btnOpenFile = Button(text="Resim Seç / Choose Image", command=OpenFile) #Dosya seçmek için OpenFile fonksiyonunu çaðýrýr.
lblTag = Label(text="{TAG}", bg="red",font="Helvetica 12") #Tanýmlanan resim etiketi bu bileþende gösterilecek.
lblImage = Label()

btnOpenFile.pack()
lblTag.pack()
lblImage.pack()

mainloop()