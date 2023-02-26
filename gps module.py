from datetime import datetime
import folium
import pandas as pd
from tkinter import *

from tkinter import messagebox as ms


def submit():
    inp = entry.get() 
    lat,lon = read(inp)
    map1(lat,lon)

def map1(a,b):

    tooltip = 'Click for more info'
    
    my_map1 = folium.Map(location = [a,b ], zoom_start = 12 )
    folium.Marker([a,b],popup='<strong>Package location</strong>',tooltip = tooltip).add_to(my_map1)
    my_map1.save(" my_map1.html " )
    
    ms.showinfo("Successful","GPS LOCATION FOUND AND HTML PAGE CREATED ")
    
def read(a):

    teraterm=pd.read_csv("gps.csv",header=None)

    teraterm.columns=['Date & Time','lat','lon']

    list_latlong = teraterm[['Date & Time','lat','lon']].values.tolist()

    for i in list_latlong:
        x_datetime = datetime.strptime(i[0], "[%Y-%m-%d %H:%M:%S.%f] ")
        curr = datetime.strftime(x_datetime, "%Y-%m-%d %H:%M:%S.%f")
        x = curr == a 
        if(x==True):
            lat = i[1]
            lon = i[2] 
            return lat,lon

    else:
        ms.showinfo("ERROR","GPS LOCATION NOT FOUND FOR THE GIVEN TIMESTAMP ")
            
window = Tk()
window.title("user input")
window.configure(width=1920,height=1080)

# Add image file
bg = PhotoImage(file = "img3.png")
  
# Create Canvas
canvas1 = Canvas( window, width = 400,height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
lab1=Label(window,text=" GENERATE GPS LOCATION ",font = ('Arial Black',20),bg="plum2",height = 2, width = 30, relief = "solid", cursor = "target")
lab1.place(x=450,y=50)


lab1=Label(window,text=" PLEASE ENTER TIME STAMP",font = ('Arial Black',12),bg="cyan",height = 2, width = 25, relief = "solid", cursor = "target")
lab1.place(x=300,y=250)


vib2=Button(window,text="Click To generate GPS location", bg='beige', font=("Arial Black", 13),height="1", width="25",borderwidth=4,relief="sunken",command=submit)
vib2.place(x=720, y=400, anchor="center")

exita=Button(window,text="EXIT ", bg='red', font=("Arial Black", 12),height="1", width="15",borderwidth=4,relief="sunken",command=window.destroy)
exita.place(x=720, y=650, anchor="center")


entry = Entry(window,width=25, font=('Arial 27'))
entry.place(x=950, y=280, anchor="center")



window.mainloop()


#2022-10-19 11:13:14.734000
