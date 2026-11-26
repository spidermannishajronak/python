import tkinter as tk

root = tk.Tk()
root.title("SMART CALCULATOR - BY RONAK")
root.geometry("340x450")
root.config(bg="#0AFC12")

text_input = tk.StringVar()
text_input.set("0")

display = tk.Entry(
   root,
   textvariable=text_input,
   font=("Arial", 22 , "bold"),
   justify="right",
   bd=8,
   relief = "ridge", 
)
display.pack(fill="x", padx = 15,pady =  15)

def click(item):
    current = text_input.get()
    if current == "0" or current == "Error":
      text_input.set( str(item))
    else:
      text_input.set(current + str(item))
      
def clear():
   text_input.set("0")
      
def calculate():
   try:
      result = eval(text_input.get())
      text_input.set(str(result))
      
   except:
      text_input.set("Error")
      
btn_frame = tk.Frame(root, bg ="#01DE08")
btn_frame.pack()


buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('.', 3, 2), ('+', 3, 3)
]    

for(text,row,col)in buttons:
   bg_color = "#00D9FF" if text == "C" else "#fbff00"
   
   btn = tk.Button(
      btn_frame,
      text=text,
      font = ("Arial", 14, "bold"),
      width=5,
      height=2,
      bg=bg_color,
      fg="dark blue",
      command= lambda t=text: clear() if t == "C" else click(t)
   )  
   btn.grid(row=row, column = col , padx=5 , pady=5)
   
   equal_btn = tk.Button(
         root,
         text="=",
         font = ("Arial",16 , "bold"),
         bg="#FFEE00",
         fg="blue",
         width=21,
         height=2,
         command= calculate
   )
equal_btn.pack(pady=10)

root.mainloop()