#pip install textblob

# Import the necessary libraries for GUI and text processing
import tkinter  # This imports the tkinter library, which is used for creating the GUI (Graphical User Interface)
from tkinter import *  # This imports everything (*) from tkinter, so we don't need to write 'tkinter.' before everything
from textblob import TextBlob  # This imports the TextBlob library, which helps with text processing, such as spelling correction

# Create the main window for the GUI application
root = Tk()  # This initializes the Tkinter window
root.title("Spelling Checker")  # Sets the title of the window to 'Spelling Checker'
root.geometry("700x400")  # Sets the size of the window to 700 pixels wide and 400 pixels tall
root.config(background="#dae6f6")  # Changes the background color of the window to a light blue shade (hex color #dae6f6)

# Define a function that will be executed when the "Check" button is clicked
def check_spelling():
    word = enter_text.get()  # 'enter_text' is the input field where the user types a word. '.get()' fetches the word entered by the user.
    a = TextBlob(word)  # We create a TextBlob object using the word entered. TextBlob helps with text processing, such as correcting spelling.
    right = str(a.correct())  # The 'correct()' method checks the spelling of the word and suggests the correct one. We convert the result to a string and store it in 'right'.

    # Create a label that shows the corrected text
    cs = Label(root, text="Correct text is:", font=("poppins", 20), bg="#dae6f6", fg="#364971")
    # This label will display "Correct text is:" with specific styles (font, size, background, and foreground colors).
    cs.place(x=100, y=250)  # The 'place()' method positions the label at x=100 and y=250 coordinates within the window.

    # Update the 'spell' label to show the corrected word
    spell.config(text=right)  # The 'spell' label gets updated with the correct word from 'right'.

# Create the heading of the application
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
# This label is the main heading of the app, with a large, bold font and the same background and text color scheme.
heading.pack(pady=(50, 0))  # 'pack()' adds the label to the window with a padding of 50 pixels at the top and 0 at the bottom.

# Create the entry box where the user will input the word to check spelling
enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
# 'Entry()' creates an input field where the user can type. We center the text, set the width, font, and background color.
enter_text.pack(pady=10)  # Adds the input field to the window with 10 pixels of padding at the top.
enter_text.focus()  # Makes the input field active and ready for typing as soon as the program starts.

# Create the "Check" button, which will trigger the check_spelling function when clicked
button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
# 'Button()' creates a button. The text on the button is "Check", styled with a specific font and colors (white text, red background).
# The 'command=check_spelling' tells the button to run the 'check_spelling()' function when clicked.
button.pack()  # Adds the button to the window.

# Create a label to display the corrected spelling result after the user clicks the "Check" button
spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
# This label will be updated later to show the correct word after the spelling check. Initially, it is empty.
spell.place(x=350, y=250)  # The label is positioned at x=350 and y=250 in the window.

# Start the Tkinter event loop (This keeps the window open and responsive)
root.mainloop()  # 'mainloop()' runs the application, waiting for events (like button clicks) to happen.

