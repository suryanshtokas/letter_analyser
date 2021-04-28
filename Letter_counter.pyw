# Import tkinter and some other libraries in it
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Import pygal, used to create the histogram
import pygal

# Import os, used to run the graph created by pygal
import os

# Define the window 
root = Tk()
# Defining the window title
root.title('Letter Counter')
# Defining the window geometry
root.geometry('601x601')
# Defining the icon for our window
root.iconbitmap('icon.ico')

a = 1

# Define a function for each button
def selectFile():
    global filename
    a = 2
    root.filename = filedialog.askopenfilename(initialdir="", title='Select a file', filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    filename=root.filename


def process():
	# Make an empty list.
	frequencies = []
	# Try to open the file that the user imported
	try:
		with open(filename, encoding='utf-8') as f_data:
			# Store the data in a variable
			contents = f_data.read()
			contents = contents.upper()
	# Accept some basic erros and tell the user what to do
	except FileNotFoundError:
		messagebox.showinfo('File Not Found', 'Please select another file')
	# If no error is there then
	# Add the frequency data to the list frequencies
	else:
		# Make a string that contains all the letters
		# Convert that string to a list
		letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
		letters_list = letters.split()
		# Make a loop that adds the data for each alphabet into a list
		for letter in letters_list:
			frequency = contents.count(letter)
			frequencies.append(frequency)
	
	# Visualize everything
	hist = pygal.Bar()

	# Name and write the x and y labels of the graph
	hist.title = 'Frequencies of the letters in your file'
	hist.x_labels = letters_list
	hist.x_title = 'Result' 
	hist.y_title = 'Frequency'

	# Add the frequencies list that we created earlier to the histogram
	hist.add('Letter', frequencies)
	# Create a file that stores our graph
	hist.render_to_file('letter_visual.svg')
	# Start the graph that we made in the above line
	os.startfile('letter_visual.svg')

# Import the background image
bgImage = PhotoImage(file='bg.png')

# Create and place a label the shows the background image
backgroundLabel = Label(root, image=bgImage)
backgroundLabel.place(x=0, y=0)

# Create and place a button that allows the user to select a file
selectFileButton = ttk.Button(root, text='Import', command=selectFile)
selectFileButton.place(x=185, y=235)

# Create and place a button that processes the file that the user imported
processFileButton = ttk.Button(root, text='Process', command=process)
processFileButton.place(x=285, y=235)

root.mainloop()


print(a)