from tkinter import *
from pytube import YouTube

#now I am creating a Display WIndow 

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Lukhele's - youtube downloader")

Label(root,text= 'Youtube Video Downloader', font='arial 20 bold').pack()


#from this point I am creating a field to enter a video link I wish to download

link = StringVar()

Label(root, text = 'Paste URL here:', font = 'arial 15 bold').place(x = 160, y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x =32, y = 90)