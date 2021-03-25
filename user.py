from tkinter import *
import tkinter as tk

lower = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
upper = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
number = ['1','2','3','4','5','6','7','8','9','0']
special = ['#','&','!','?','@']


def check():
    password = inp.get()
    l, u, n, s = 0, 0, 0, 0
    if (len(password)<=18) and (len(password)>=8):
        for x in password:

            if (x in lower):
                l=l+1
            elif (x in upper):
                u=u+1
            elif (x in number):
                n=n+1
            elif (x in special):
                s=s+1
            
    if (l>=1 and u>=1 and n>=1 and s>=1):
        print('Valid !')
        inp.delete(0,tk.END)
        
        window = tk.Toplevel()

        label = tk.Label(window, text="Valid !",font=("Arial", 25))
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(window, text="Close", command=window.destroy,font=("Arial", 20))
        button_close.pack(fill='x')
        
    else:
        
        inp.delete(0,tk.END)
        
        window = tk.Toplevel()

        label = tk.Label(window, text="Invalid !",font=("Arial", 25))
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(window, text="Close", command=window.destroy,font=("Arial", 20))
        button_close.pack(fill='x')

validator = tk.Tk()
validator.geometry("600x500")
label = tk.Label(validator,font=("Arial", 25), text='Rules for your password \n '
         +'Length between 8 and 18 characters \n'
         +'Must contain at least : \n'
         +' - 1 lowercase letter \n'
         +' - 1 uppercase letter \n'
         +' - 1 number \n '
         +' - 1 special sign(# & ! @ ?)').grid(row=0,pady = 10)



inp = tk.Entry(validator,font=("Arial", 25))

inp.grid(row=2, column=0)



submit = Button(validator, font=("Arial", 25),
          text='Submit', command=check).grid(row=3, column=0, pady=4)

tk.mainloop()
