# main.py

import tkinter as tk  # Import tkinter module

# Import your FrigorificoApp from interfaz.py
from interfaz import FrigorificoApp

if __name__ == "__main__":
    root = tk.Tk()  # Create a Tk instance using tk.Tk()
    app = FrigorificoApp(root)  # Pass the Tk instance to your application
    root.mainloop()  # Start the tkinter main event loop