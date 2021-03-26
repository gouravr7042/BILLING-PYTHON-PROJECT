from tkinter import *

window = Tk()
window.geometry("800x700")

def calculate():
    paneer_tikka=e1.get()
    chicken_tanduri=e2.get()
    chicken_briyani=e3.get()
    korma_parata=e4.get()

    total = ((int(paneer_tikka)*150)+(int(chicken_tanduri)*350)+(int(chicken_briyani)*180)+(int(korma_parata)*105))
    label12 = Label(window, text=total, font="times 25 bold")
    label12.place(x=200,y=440)

label6 = Label(window, text="ANNAPURNA RESTURANT", font="times 25 bold")
label6.place(x=180, y=20)

#------------menu option ------------#
label1 = Label(window, text="MENU", font="times 22 bold")
label1.place(x=550, y=70)

label2 = Label(window,text=" Paneer Tikka           RS.150",font="times 20 bold")
label2.place(x=450, y=120)

label2 = Label(window,text=" Chicken Tanduri     RS.350",font="times 20 bold")
label2.place(x=450, y=150)

label2 = Label(window,text=" Chicken Briyani      RS.180",font="times 20 bold")
label2.place(x=450, y=180)

label2 = Label(window,text=" Korma Parata         RS.105",font="times 20 bold")
label2.place(x=450, y=210)

label7 = Label(window, text="Select the Items", font="times 20 bold")
label7.place(x=80, y=90)

label8 = Label(window, text="Panner Tikka", font="time 18  bold")
label8.place(x=20, y=140)

e1 = Entry(window)
e1.place(x=20, y=180)

label8 = Label(window, text="Chikcen Tanduri", font="time 18  bold")
label8.place(x=250, y=140)

e2 = Entry(window)
e2.place(x=250, y=180)

label8 = Label(window, text="Chicken Briyani", font="time 18  bold")
label8.place(x=20, y=220)

e3 = Entry(window)
e3.place(x=20, y=250)

label8 = Label(window, text="Korma parata", font="time 18  bold")
label8.place(x=250, y=215)

e4 = Entry(window)
e4.place(x=250, y=250)

b2 = Button(window, text="BILL", font="time 20 bold",width = 20,command=calculate)
b2.place(x=100, y=350)
window.mainloop()



