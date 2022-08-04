
from tkinter import *

import speedtest

# Function to check speed and assign the values to variable
def speed():
  sp = speedtest.Speedtest()
  sp.get_servers()
  down = str(round(sp.download()/(10**6), 3)) + " Mbps"
  up = str(round(sp.upload()/(10**6), 3)) + " Mbps"
  lab_D.config(text=down)
  lab_U.config(text=up)

# Main Heading 
sp = Tk()
sp.title("Check your Internet Speed!")
sp.geometry("400x400")

sp.config(bg= "Green")

lab = Label(sp, text = "Internet Speed Test", font= ("Times New Roman", 30, "bold"), bg="Green", fg="White")
lab.place(x=10,y=30, height=30, width= 380)

# Download Speed Function call 

lab = Label(sp, text = "Download Speed", font= ("Times New Roman", 25, "bold"), bg="Green", fg="White")
lab.place(x=20,y=120, height=30, width= 380)

lab_D = Label(sp, text = "00", font= ("Times New Roman", 20, "bold"), bg="Green", fg="White")
lab_D.place(x=20,y=170, height=30, width= 380)

# Upload Speed 

lab = Label(sp, text = "Upload Speed", font= ("Times New Roman", 25, "bold"), bg="Green", fg="White")
lab.place(x=20,y=220, height=30, width= 380)

lab_U = Label(sp, text = "00", font= ("Times New Roman", 20, "bold"), bg="Green", fg="White")
lab_U.place(x=20,y=270, height=30, width= 380)

#  button for calling speed() function 

button = Button(sp, text= "Check Speed", font=("Times New Roman", 15, "bold"),relief= RAISED, command= speed)
button.place (x=151,y=320, height=40, width= 120)

sp.mainloop()
