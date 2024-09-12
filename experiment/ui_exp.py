import tkinter as tk


def button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Tkinter UI Experiment")
root.geometry("800x600")

label = tk.Label(root, text="Hello, World!")
label.grid(row=0, column=0)
label1 = tk.Label(root, text="Sajtból van a Hold!")
label1.grid(row=0, column=1)

button = tk.Button(root, text="Button", command=button_click)
button.grid(row=1, column=0)


root.mainloop()