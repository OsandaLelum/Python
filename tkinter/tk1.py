import tkinter as tk

def on_button_click():
    print("Button clicked!")

if __name__ == '__main__':
    # Create the main window
    window = tk.Tk()
    window.title("Tkinter Example")
    window.geometry("300x200")

    # Create a button
    button = tk.Button(window, text="Click me", command=on_button_click)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Start the Tkinter event loop
    window.mainloop()

