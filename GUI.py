import tkinter
from cashregister import *
from dispenser import *
window = tkinter.Tk()
window.title("Candy Machine")
window.geometry("300x300")
window.configure(bg='light green')
machine = tkinter.Label(window,
            text="**** Welcome to Sweet's Candy Shop ****",
            fg = "black",
            bg = "light green",
            font = "Helvetica 12 bold italic")
machine.pack()
label = tkinter.Label(window,
            text="Please make a selection",
            fg = "black",
            bg = "light green",
            font = "Helvetica 10 bold italic")
label.pack()
def new():
    newwindow = tkinter.Tk()
    newwindow.title("Sweet's Candy Machine")
    newwindow.geometry("300x300")
    newwindow.configure(bg='light green')
    label = tkinter.Label(newwindow,
                          text = "Ready to Purchase",
                          fg = "black",
                          bg = "light green",
                          font = "Helvetica 10 bold italic")
    label.pack()
    choosen = Dispenser()
    count = choosen.getCount()
    x = choosen.getProductcost()
    lbl = tkinter.Label(newwindow,
                        text="To purchase please insert Amount" + str({x}),
                        fg="black",
                        bg="light green",
                        font="Helvetica 10 bold italic")
    lbl.pack()
    amt = tkinter.Entry(newwindow)
    amt.pack()

    def new1():
        balance=500
        amount = int(amt.get())
        amount
        choosen = Dispenser()
        x = int(choosen.getProductcost())
        cash = CashRegister()
        cash.acceptAmount(amount)
        cash.CashRegister(x)
        if amount > x:
            change = tkinter.Label(newwindow,
                                       text="Please get your change:" + str(amount - x),
                                       fg="black",
                                       bg="light green",
                                       font="Helvetica 10 bold italic")
            change.pack()
            ready = tkinter.Label(newwindow,
                                      text="Your Item is Ready please get it in the dispenser",
                                      fg="black",
                                      bg="light green",
                                      font="Helvetica 10 bold italic")
            ready.pack()
            thanks = tkinter.Label(newwindow,
                                       text="thank you for purchasing",
                                       fg="black",
                                       bg="light green",
                                       font="Helvetica 10 bold italic")
            thanks.pack()
            if (int(amount) - int(x)) == 0:
                ready = tkinter.Label(newwindow,
                                      text="Your Item is Ready please get it in the dispenser",
                                      fg="black",
                                      bg="light green",
                                      font="Helvetica 10 bold italic")
                ready.pack()
                thanks = tkinter.Label(newwindow,
                                       text="thank you for purchasing",
                                       fg="black",
                                       bg="light green",
                                       font="Helvetica 10 bold italic")
                thanks.pack()
            if amount == 0:
                thanks = tkinter.Label(newwindow,
                                       text="Insufficient Amount",
                                       fg="black",
                                       bg="light green",
                                       font="Helvetica 10 bold italic")
                thanks.pack()
                ready = tkinter.Label(newwindow,
                                      text="Your Item is Ready please get it in the dispenser",
                                      fg="black",
                                      bg="light green",
                                      font="Helvetica 10 bold italic")
                ready.pack()
                redu = tkinter.Label(newwindow,
                                     text="Amount is reduced in the balanced",
                                     fg="black",
                                     bg="light green",
                                     font="Helvetica 10 bold italic")
                redu.pack()
                thanks = tkinter.Label(newwindow,
                                       text="thank you for purchasing",
                                       fg="black",
                                       bg="light green",
                                       font="Helvetica 10 bold italic")
                thanks.pack()


    bttn = tkinter.Button(newwindow,
                             text="Ok",
                             fg="black",
                             bg="white",
                             width=15,
                          command=new1)
    bttn.pack()
    bttn = tkinter.Button(newwindow,
                             text="Back",
                             fg="black",
                             bg="white",
                             width=15,
                          command=newwindow.destroy)
    bttn.pack(side=tkinter.BOTTOM)



button1 = tkinter.Button(window,
                             text="A. Candy",
                             fg="black",
                             bg="white",
                             width=25,
                         command=new)

button2 = tkinter.Button(window,
                             text="B. Chips",
                             fg="black",
                             bg="white",
                             width=25,
                             command=new)

button3 = tkinter.Button(window,
                             text="C. Gums",
                             fg="black",
                             width=25,
                             command=new)

button4 = tkinter.Button(window,
                             text="D. Cookies",
                             fg="black",
                             bg="white",
                             width=25,
                             command=new)

button5 = tkinter.Button(window,
                             text="E. Exit",
                             fg="black",
                             bg="white",
                             width=25,
                             command=window.destroy)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

window.mainloop()