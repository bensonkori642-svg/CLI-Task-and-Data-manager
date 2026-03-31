import tkinter
button_values=[
    ["AC","+/-","%","/"],
    ["7","8","9","*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","1/1/2","="],
]
right_symbols=["/","*","-","+","="]
top_symbols=["AC","+/-","%"]

row_count=len(button_values)
column_count=len(button_values[0])

light_grey="AD4D4D2"
color_black="A1C1C1C"
color_dark_grey="#505050"
color_orange="#FF9500"
color_white="white" 

window=tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)
window.mainloop()
frame=tkinter.Frame(window)
label=tkinter.Label(frame, text="0",font=("Arial",45),foreground=black)
buttons=tkinter.Button(window)
label.pack()
frame.pack()


