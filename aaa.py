import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Simple UI Example")

# Create a label
label = tk.Label(window, text="Hello, this is a simple UI!")

# Create a button
button = tk.Button(window, text="Click me!", command=on_button_click)

# Place the label and button in the window
label.pack(pady=10)
button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
