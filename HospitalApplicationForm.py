import tkinter as tk
root = tk.Tk()
root.geometry("500x300")

def add_contact():
    text = text_box1.get("1.0", "end-1c")
    text_box_m1.insert("end", text)
    text1 = text_box2.get("1.0", "end-1c")
    text_box_m2.insert("end", text1)
    text2 = text_box3.get("1.0", "end-1c")
    text_box_m3.insert("end", text2)

Name = tk.Label(root, text="Name").place(x=0,y=0)
text_box1 = tk.Text(root, height=1, width=15)
text_box1.place(x=50,y=0)

City = tk.Label(root, text="City").place(x=0,y=20)
text_box2 = tk.Text(root, height=1, width=15)
text_box2.place(x=50,y=20)


Street = tk.Label(root, text="Street").place(x=0,y=40)
text_box3 = tk.Text(root, height=1, width=15)
text_box3.place(x=50,y=40)


button_Retrieve = tk.Button(root, text="Retrieve All").place(x=0,y=60)
button_Add = tk.Button(root, text="Add",command=add_contact).place(x=75,y=60)
button_Remove = tk.Button(root, text="Remove").place(x=120,y=60)
button_Clear = tk.Button(root, text="Clear").place(x=180,y=60)
button_Table = tk.Button(root, text="Clear Table Widget").place(x=220,y=60)
button_Entry = tk.Button(root, text="Clear Entry Widgets").place(x=330,y=60)

text_box_m1 = tk.Text(root, height=12, width=20)
text_box_m1.place(x=0,y=90)
text_box_m2 = tk.Text(root, height=12, width=20)
text_box_m2.place(x=150,y=90)
text_box_m3 = tk.Text(root, height=12, width=20)
text_box_m3.place(x=300,y=90)

root.mainloop()