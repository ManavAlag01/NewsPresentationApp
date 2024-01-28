from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Newspaper-Purani khabar ke Saat Apka Manav")
root.geometry("700x500")  # Increased the width to accommodate the text

my_label1 = Label(text="Purani Khbhar k Saat Apka Manav", fg="black", font="cosmicsansms 30 bold")
my_label1.pack(pady=10)

my_label2 = Label(text="Date:-15th January, 2024", fg="black", font="cosmicsansms 20")
my_label2.pack()

# Load the original image
original_image = Image.open("virat.png")
original_image1 = Image.open("rohit.png")
                                      
# Resize the image to the desired size (e.g., 200x200)
desired_size = (260, 260)
resized_image = original_image.resize(desired_size, Image.LANCZOS)
desired_size1 = (300, 300)
resized_image1 = original_image1.resize(desired_size1, Image.LANCZOS)

# Convert the PIL Image to a Tkinter PhotoImage
photo_image = ImageTk.PhotoImage(resized_image)

viratlabel = Label(root, image=photo_image, text='''Virat has received many accolades for his performances in cricket. He was recognized as the ICC ODI Player of the Year in 2012 and has won the Sir Garfield Sobers Trophy, given to the ICC Cricketer of the Year, on two occasions, in 2017 and 2018 respectively. Subsequently, Kohli also won ICC Test Player of the Year and ICC ODI Player of the Year awards in 2018'''
                   ,compound="right", wraplength=850, font="cosmicsansms 20 bold", padx=100)
# viratlabel.pack(anchor="nw", pady=50)
viratlabel.pack()
photo_image1 = ImageTk.PhotoImage(resized_image1)

rohitlabel = Label(root, image=photo_image1, text="Sharma formerly captained Mumbai Indians and the team has won 5 titles in 2013, 2015, 2017, 2019 and 2020 under his leadership, making him the most successful captain in IPL history, sharing this record with MS Dhoni (5 title wins in IPL). With India, Sharma was a member of the team that won the 2007 T20 World Cup, and the 2013 ICC Champions Trophy"
                   ,compound="left", wraplength=850, font="cosmicsansms 20 bold", padx=10)
rohitlabel.pack(side="bottom", anchor="sw", pady=10, padx=10)  # Using pack instead of grid

root.mainloop()
