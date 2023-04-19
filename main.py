import tkinter as tk
import datetime as dt
from student import Student

#Global Variables
current = dt.datetime.now().strftime("%H:%M %m/%d/%y")
print(current)

#filename
path = "test.csv"


# Global functions
# Load file
def loadFile():
  pass


# Save file
def saveFile():
  pass

# Function for capturing what is entered in the entry box then creating a student object.
# Function for updating widgets for each Student.

window = tk.Tk()

# Global TK settings
window.title("Waddle Counter")
window.geometry("300x300")

# Create tk widgets

heading = tk.Label(text="Steampunk Penguins Attendence")
entryBox = tk.Entry()
submit = tk.Button(text="Submit")
timestamp = tk.Label(text=current)
atdFrame = tk.Frame()

#Grid arrangment for the GUI
heading.grid(row=1, column=1, columnspan=3)
entryBox.grid(row=2, column=1)
submit.grid(row=2, column=2)
timestamp.grid(row=2, column=3)
atdFrame.grid(row=3, column=1, columnspan=3)

tk.mainloop()
