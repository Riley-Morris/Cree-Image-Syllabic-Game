#TODO - FIX BUG, can change butt1 image in function to something else - creates weirder bug.... need to store initial stuff differently? and its almost like its not getting deleted.

from tkinter import *
from PIL import ImageTk, Image
import os
import random

root = Tk()

root.title('Test App')
root.iconbitmap(r"C:\Users\riley\Documents\Pyth\CreeImageGame\Icon\CrowIcon.ico")
imagen = 'Start.png'

image_list = []
button_list=[]
#make list of images in directory
for file in os.listdir('Images'):
    image_list.append(file)
#remove start image from list
image_list.remove('Start.png')


# function to generate correct images for buttons (1 correct 3 randoms)
def button_image_gen():
    global button_list
    button_list = []
    m_list = []
    for file in os.listdir('Images'):
        m_list.append(file)

    # remove correct answer from master list
    m_list.remove(imagen)
    m_list.remove('Start.png')
    # add 3 random image names to button list
    button_list.append(m_list.pop())
    button_list.append(m_list.pop())
    button_list.append(m_list.pop())
    # append correct answer randomly
    button_list.insert(random.randint(0, len(button_list)), imagen)

#main function for changing screen on button click
def change_screen():
    global image_list
    global imagen
    global img_label
    global image1
    global butt1_label
    global butt1_img
    global button1
    global butt2_label
    global butt3_label
    global butt4_label
    global butt2_img
    global butt3_img
    global butt4_img
    global button2
    global button3
    global button4
    global button_list

    #forget the label for image
    img_label.grid_forget()
    #destory old buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    #pop off next image from list
    imagen = image_list.pop(random.randrange(0, len(image_list)))
    # generate buttons
    button_image_gen()
    #redefine image
    image1 = ImageTk.PhotoImage(Image.open(f'Images/{imagen}'))
    img_label = Label(image=image1)
    img_label.grid(row=0, column=0, columnspan = 3)

    #change buttons
    butt1_img = PhotoImage(file = f'ImageSyllabics/{button_list[0]}')
    butt1_label = Label(image=butt1_img)
    button1 = Button(root, image=butt1_img, command=lambda: change_screen())
    button1.grid(row=2, column=1)

    butt2_img = PhotoImage(file=f'ImageSyllabics/{button_list[1]}')
    butt2_label = Label(image=butt2_img)
    button2 = Button(root, image=butt2_img, command=lambda : change_screen())
    button2.grid(row=2, column=2)

    butt3_img = PhotoImage(file = f'ImageSyllabics/{button_list[2]}')
    butt3_label = Label(image = butt3_img)
    button3 = Button(root, image=butt3_img, command=lambda : change_screen())
    button3.grid(row=3, column=1)

    butt4_img = PhotoImage(file = f'ImageSyllabics/{button_list[3]}')
    butt4_label = Label(image = butt4_img)
    button4 = Button(root, image=butt4_img, command=lambda : change_screen())
    button4.grid(row=3, column=2)



image1 = ImageTk.PhotoImage(Image.open(f'Images/{imagen}'))
img_label = Label(image = image1)
img_label.grid(row = 0, column = 0, columnspan = 3)

#create initial buttons
butt1_img = PhotoImage(file="Icon/Butt1.png")
butt1_label = Label(image=butt1_img)
button1 = Button(root, image=butt1_img, command=lambda : change_screen())
button1.grid(row=2, column=0)

butt2_img = PhotoImage(file="Icon/Butt1.png")
butt2_label = Label(image=butt2_img)
button2 = Button(root, image=butt2_img, command=lambda : change_screen())
button2.grid(row=2, column=1)

butt3_img = PhotoImage(file="Icon/Butt1.png")
butt3_label = Label(image=butt3_img)
button3 = Button(root, image=butt3_img, command=lambda : change_screen())
button3.grid(row=3, column=0)

butt4_img = PhotoImage(file="Icon/Butt1.png")
butt4_label = Label(image=butt4_img)
button4 = Button(root, image=butt4_img, command=lambda : change_screen())
button4.grid(row=3, column=1)

root.mainloop()