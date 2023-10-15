#Prodigy Infotech Intership
# TASK 1 Temperature conversion
# A.Without using tkinter

while True:
    print('\nHello sir/mam,\n')
    print('\t\tThis program converts temperature between Celsius, Fahrenheit, and Kelvin scale. \n')

    a = input('Enter C for Celsius, F for Fahrenheit, or K for Kelvin: ')

    if a.lower()== 'q' : 
        break

    match a.lower():
        case "c":
            celsius = float(input("Enter the temperature in Celsius: "))
            print("The temperature in Celsius is", celsius)
            print("The temperature in Kelvin is", celsius + 273.15)
            print("The temperature in Fahrenheit is", (celsius * 9/5) + 32)
        
        case "f":
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            print("The temperature in Fahrenheit is", fahrenheit)
            celsius = (fahrenheit - 32) * 5/9
            print("The temperature in Celsius is", celsius)
            print("The temperature in Kelvin is", celsius + 273.15)

        case "k":
            kelvin = float(input("Enter the temperature in Kelvin: "))
            print("The temperature in Kelvin is", kelvin)
            celsius = kelvin - 273.15
            print("The temperature in Celsius is",celsius)
            print("The temperature in Fahrenheit is", (celsius * 9/5) + 32)    
        
        case _:
            print("Invalid input!")
            print("Please enter C, F, or K as given in the instructions.")
   
    
# B. Using tkinter        

from tkinter import *

root=Tk()
root.title("Temperature conversion")
root.geometry("400x300")

def convert1():
    temp=int(Centigrade.get())
    label=Label(text=f"Given temperature in celsius is {temp}")
    label.pack()
    label1 =Label(root,text=f"The temperature in fahrenheit is {(temp*9/5)+32}")
    label1.pack()
    label2 =Label(root,text=f"The temperature in Kelvin is {temp+273}")
    label2.pack()
    Centigrade.delete(0, END)   

def centigrade():
    label=Label(root,text="Ener the temperature in Centigrade")
    label.pack(pady=15)
    global Centigrade
    Centigrade=Entry(root)
    Centigrade.pack()
    buttom=Button(text="Convert",command=convert1)
    buttom.pack()


def convert2():
    temp=int(Fahrenheit.get())
    label=Label(text=f"Given temperature in fahrenheit is {temp}")
    label.pack
    celsius = (temp - 32) * 5/9
    label1 =Label(text=f"The temperature in celsius is {celsius}")
    label1.pack()
    label2 =Label(text=f"The temperature in Kelvin is {celsius+273}")
    label2.pack()
    Fahrenheit.delete(0, END)  

def fahrenheit():
    label=Label(root,text="Ener the temperature in fahrenheit")
    label.pack(pady=15)
    global Fahrenheit
    Fahrenheit=Entry(root)
    Fahrenheit.pack()
    buttom=Button(text="Convert",command=convert2)
    buttom.pack()

def convert3():
    temp=int(Kelvin.get())
    label=Label(text=f"Given temperature in Kelvin is {temp}")
    label.pack
    label1 =Label(text=f"The temperature in Celsius is {temp-273}")
    label1.pack()
    celsius = temp - 273.15
    label2 =Label(text=f"The temperature in fahrenheit is {(celsius * 9/5) + 32}")
    label2.pack()
    Kelvin.delete(0, END)   

def kelvin():
    label=Label(root,text="Ener the temperature in Kelvin")
    label.pack(pady=15)
    global Kelvin
    Kelvin=Entry(root)
    Kelvin.pack()
    buttom=Button(text="Convert",command=convert3)
    buttom.pack()


f1=Frame(root)
f1.pack()
label=Label(f1,text="Choose the unit of the temperature")
label.pack()

buttom=Button(f1,text="Centigrade",command= centigrade)
buttom.pack(side=LEFT,padx=30)
buttom=Button(f1,text="Fahrenheit",command=fahrenheit)
buttom.pack(side=LEFT,padx=30)
buttom=Button(f1,text="Kelvin",command=kelvin)
buttom.pack(side=LEFT,padx=30)


root.mainloop()




