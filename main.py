"""
WinterChoiceProject 
Author: Cara Tiller 
Garrett Tiller
"""
# I currently have this as a comment because it is not working. 
import datetime

import tkinter as tk
from PIL import Image,ImageTk 

window=tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ") 

name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
def getInput():
    name=nameEntry.get()
    persons_name = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Heyy {persons_name}!!!. You are {age} years old!!! ".format(persons_name=name, age=persons_name.age())
    textArea.insert(tk.END,answer)
button=tk.Button(window,text="Calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=5)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
"""image=Image.open('unnamed.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)"""
window.mainloop()


from PIL import Image,ImageTk  
image = Image.open('Path' )    
image.thumbnail((100,100),Image.ANTIALIAS)   

photo= ImageTk.PhotoImage(image)   
label_image= tk.Label(image=photo)  
label_image.grid(column=1,row=0) 
"""
print("EXAMPLE:\nWhat Year Where You Born? 2005 \nWhat Month Where You Born? 11 \nWhat Day Where You Born? 22 \nHow many Leap Year Have You Had In Your Lifetime? 4\nEnter The Current Year: 2020\nEnter the Current Month: 12\nEnter the Current Day: 17\nYou Have Been Alive For 5,504 Days !\nNow Enter Your Birthday !")

birth_year= int(input("What Year Where You Born? "))
birth_month= int(input("What Month Where You Born? "))
birth_day= int(input("What Day Where You Born? "))
leap_year = int(input("How Many Leap Years Have You Had In Your Lifetime? "))
current_year= int(input("Enter The Current Year: "))
current_month=input("Enter The Current Month: ")
current_day=int(input("Enter The Current Day: "))

def month():
  if current_month=1 : 
    y=0
  elif current_month = 2: #feb
    y=31
  elif current_month = 3: #march
    y=59
  elif current_month = 4: #apirl
    y=90
  elif current_month = 5: 
    y=121 #may
  elif current_month =6: 
    y=151#june
  elif current_month = 7:
    y=181 #july
  elif current_month = 8:
    y=212 #august
  elif current_month =9:
    243 #sept
  elif current_month =10:
    y=273 #oct
  elif current_month =11:
    y=304 #nov
  elif current_month =12:
    y=334 #dec

x=current_year-birth_year """