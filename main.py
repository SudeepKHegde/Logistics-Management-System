from tkinter import *
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import folium
import pandas as pd
from tkinter import messagebox as ms


def tempfunc():
    x = []
    y = []
    z = []
    a = []
    b = []
      
    with open('teraterm.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
            z.append(int(row[2]))
            a.append(int(row[3]))
            b.append(int(row[4]))
      


    #plt.plot(x, y, label = "VIBRATION SENSOR 1 ")
    #plt.plot(x, z, label = "VIBRATION SENSOR 2 ")
    plt.plot(x, a, label = "TEMPRATURE SENSOR ")
    #plt.plot(x, b, label = "HUMIDITY SENSOR ")
    plt.legend()
    plt.title("TEMPRATURE ANALYSIS")
    plt.xlabel("TIME STAMP")
    plt.ylabel("PARAMETER")
    plt.show()


def humfunc():
    x = []
    y = []
    z = []
    a = []
    b = []
      
    with open('teraterm.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
            z.append(int(row[2]))
            a.append(int(row[3]))
            b.append(int(row[4]))
      


    #plt.plot(x, y, label = "VIBRATION SENSOR 1 ")
    #plt.plot(x, z, label = "VIBRATION SENSOR 2 ")
    #plt.plot(x, a, label = "TEMPRATURE SENSOR ")
    plt.plot(x, b, label = "HUMIDITY SENSOR ")
    plt.legend()
    plt.title("HUMIDITY ANALYSIS")
    plt.xlabel("TIME STAMP")
    plt.ylabel("PARAMETER")
    plt.show()


def vibfunc1():
    x = []
    y = []
    z = []
    a = []
    b = []
      
    with open('teraterm.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
            z.append(int(row[2]))
            a.append(int(row[3]))
            b.append(int(row[4]))
      


    plt.plot(x, y, label = "VIBRATION SENSOR 1 ")
    #plt.plot(x, z, label = "VIBRATION SENSOR 2 ")
    #plt.plot(x, a, label = "TEMPRATURE SENSOR ")
    #plt.plot(x, b, label = "HUMIDITY SENSOR ")
    plt.legend()
    plt.title("VIBRATION ANALYSIS")
    plt.xlabel("TIME STAMP")
    plt.ylabel("PARAMETER")
    plt.show()

def vibfunc2():
    x = []
    y = []
    z = []
    a = []
    b = []
      
    with open('teraterm.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
            z.append(int(row[2]))
            a.append(int(row[3]))
            b.append(int(row[4]))
      


    #plt.plot(x, y, label = "VIBRATION SENSOR 1 ")
    plt.plot(x, z, label = "VIBRATION SENSOR 2 ")
    #plt.plot(x, a, label = "TEMPRATURE SENSOR ")
    #plt.plot(x, b, label = "HUMIDITY SENSOR ")
    plt.legend()
    plt.title("VIBRATION ANALYSIS")
    plt.xlabel("TIME STAMP")
    plt.ylabel("PARAMETER")
    plt.show()

def allgfunc():
    x = []
    y = []
    z = []
    a = []
    b = []
      
    with open('teraterm.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            x.append(row[0])
            y.append(int(row[1]))
            z.append(int(row[2]))
            a.append(int(row[3]))
            b.append(int(row[4]))
      


    plt.plot(x, y, label = "VIBRATION SENSOR 1 ")
    plt.plot(x, z, label = "VIBRATION SENSOR 2 ")
    plt.plot(x, a, label = "TEMPRATURE SENSOR ")
    plt.plot(x, b, label = "HUMIDITY SENSOR ")
    plt.legend()
    plt.title("ALL PARAMETER ANALYSIS")
    plt.xlabel("TIME STAMP")
    plt.ylabel("PARAMETER")
    plt.show()


        
    
window=Tk()

window.title("PACKAGE DATA MANAGMENT PLOTS")

window.configure(width=1920,height=1080)


# Add image file
bg = PhotoImage(file = "img3.png")
  
# Create Canvas
canvas1 = Canvas( window, width = 1920,height = 1080)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")


lab1=Label(window,text=" LMS CONTROL PANEL",font = ('Arial Black',20),bg="plum2",height = 2, width = 25, relief = "solid", cursor = "target")
lab1.place(x=500,y=50)


    
temp=Button(window,text="SHOW TEMPRATURE SENSOR DATA", bg='beige', font=("Arial Black", 13),height="1", width="30",borderwidth=4,relief="sunken",command=tempfunc)
temp.place(x=500, y=250, anchor="center")

hum=Button(window,text="SHOW HUMIDITY SENSOR DATA", bg='beige', font=("Arial Black", 13),height="1", width="30",borderwidth=4,relief="sunken",command=humfunc)
hum.place(x=500, y=370, anchor="center")

vib1=Button(window,text="SHOW VIBRATION SENSOR - 1 DATA", bg='beige', font=("Arial Black", 13),height="1", width="30",borderwidth=4,relief="sunken",command=vibfunc1)
vib1.place(x=1000, y=250, anchor="center")

vib2=Button(window,text="SHOW TEMPRATURE SENSOR -2 DATA", bg='beige', font=("Arial Black", 13),height="1", width="30",borderwidth=4,relief="sunken",command=vibfunc2)
vib2.place(x=1000, y=370, anchor="center")

allg=Button(window,text="SHOW ALL SENSOR DATA", bg='beige', font=("Arial Black", 13),height="1", width="30",borderwidth=4,relief="sunken",command=allgfunc)
allg.place(x=720, y=500, anchor="center")



exita=Button(window,text="EXIT ", bg='red', font=("Arial Black", 13),height="1", width="20",borderwidth=4,relief="sunken",command=window.destroy)
exita.place(x=720, y=650, anchor="center")

window.mainloop()
