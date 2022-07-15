
#TODO - Implement buttons matching up to wrong answers and store it
# system to display and store result of choice. Second Window inbetween or on correct/incorrect on bottom?

import os, random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#app title
root.title('Eastern Cree Syllabic Game')
#icon for application
root.iconbitmap(r"C:\Users\riley\Documents\Pyth\CreeImageGame\Icon\CrowIcon.ico")

#default start image
defaultimg = ImageTk.PhotoImage(Image.open('Icon/crowiconraw.jpg'))
defaultlabel = Label(image = defaultimg)
defaultlabel.grid(row = 0, column = 0)

#correct choice
b_correct = ''
#list of image files
f_list = []

#iterate over files in current directory to create f_list
for filename in os.listdir('Images'):
    f = os.path.join(filename)
    f_list.append(f)






#function code for button to answer and go to next question, will select next randomly
def answer():
    global defaultlabel
    global defaultimg
    global b_correct

    global f_list

    #select random number from length of image list
    numchoice = random.randint(0, len(f_list)-1)
    #actually select image
    defaultimg = ImageTk.PhotoImage(Image.open(f'Images/{f_list[numchoice]}'))
    #put image into a label
    defaultlabel = Label(image = defaultimg)
    #put label onto root window
    defaultlabel.grid(row = 0, column = 0)
    #will store correct choice as current image name
    root_correct = os.path.splitext(f'Images/{f_list[numchoice]}')
    # remove correct choice from list to avoid duplication
    f_list.remove(f_list[numchoice])
    #split this into the base name of the answer file - ex seagulls.jpg ----> Seagullsyl.png
    b_correct = root_correct[0].split('Images/')[1] +'syl' + '.png'
    print(b_correct)

#function for button choice
def button_gen():
    global b_choice
    #generate a list of 3 possible other answers to put into buttons
    wrong_answers = random.sample(f_list, 3)
    print(wrong_answers)


answer()
button_gen()

butt1img = PhotoImage(file="ImageSyllabics/Beaversyl.png")
butt1label = Label(image = butt1img)
button1 = Button(root, image = butt1img, command = )
button1.grid(row = 2, column = 0)

root.mainloop()