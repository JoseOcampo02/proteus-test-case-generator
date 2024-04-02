import tkinter as tk
from App import App  # Make sure the App class is correctly imported

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
