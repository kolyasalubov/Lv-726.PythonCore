from tkinter import *
from tkinter import messagebox

"""
(str) -> str

Write a program that calculates the area of ​a rectangle, 
triangle and circle 
(write three functions to calculate the area, and call them in the 
main program depending on the user's choice) 
"""


def rectangle_area():
    a = int(entry_a.get())
    b = int(entry_b.get())
    s = a*b
    # res_lbl_rec.configure(text=f"Rectangle Area is {s:.2f}")
    messagebox.showinfo('Rectangle Area',f"Result is {s:.2f}")

def triangle_area():
    a = int(entry_a.get())
    b = int(entry_b.get())
    c = int(entry_c.get())
    p = (a+b+c)/2
    s = ((p*(p-a)*(p-b)*(p-c))**0.5)
    if isinstance(s, complex):
        messagebox.showinfo('Triangle Area',f'You have ' \
                            f'entered incorrect data') 
    # this is so that the line of code does not exceed 79 characters.
    
    else:
        messagebox.showinfo('Triangle Area',f"Result is {s:.2f}")
    # res_lbl_trg.configure(text=f"Triangle Area is {s:.2f}")

def circle_area():
    r = int(entry_r.get())
    PI = 3.14
    s = PI*(r**2)
    # res_lbl_crl.configure(text=f"Circle Area is {s:.2f}")
    messagebox.showinfo('Circle Area',f"Result is {s:.2f}")   
 
root = Tk()     
root.title("Area program")     
root.geometry("400x150")   

# res_lbl_rec = Label(root, text="")
# res_lbl_rec.grid(column=3,row=0)
# res_lbl_trg = Label(root, text="")
# res_lbl_trg.grid(column=3,row=1)
# res_lbl_crl = Label(root, text="")
# res_lbl_crl.grid(column=3,row=2)
info_label_rec = Label(text="Rectangle has only sides  'a' and 'b'")
info_label_rec.grid(column=4,row=0)
info_label_trg = Label(text="Triangle has  sides  'a','b' and 'c'")
info_label_trg.grid(column=4,row=1)
info_label_crl = Label(text="For circle input only 'R'")
info_label_crl.grid(column=4,row=3)


label_a = Label(text="Enter a:") 
label_a.grid(column=0,row=0)
label_b = Label(text="Enter b:") 
label_b.grid(column=0,row=1)
label_c = Label(text="Enter c:") 
label_c.grid(column=0,row=2)
label_r = Label(text="Enter R:") 
label_r.grid(column=0,row=3)

entry_a = Entry(root,width=3)  
entry_a.grid(column=1, row=0)
entry_b = Entry(root,width=3)  
entry_b.grid(column=1, row=1)
entry_c = Entry(root,width=3)  
entry_c.grid(column=1, row=2)
entry_r = Entry(root,width=3)  
entry_r.grid(column=1, row=3)


btn_rec = Button(root, text="Rectangle area", command=rectangle_area)  
btn_rec.grid(column=2, row=0)

btn_trg = Button(root, text="Triangle area", command=triangle_area)  
btn_trg.grid(column=2, row=1)

btn_crl = Button(root, text="Circle area", command=circle_area)  
btn_crl.grid(column=2, row=3)


root.mainloop()


