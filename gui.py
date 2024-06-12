import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy
import numpy as np

#loading the models
from keras.models import load_model
model=load_model('Model-age-gender_detector.keras')

#iitializing gui
top=tk.Tk()
top.geometry('800x600')
top.title('Age and gender detector')
top.configure(background='#CDCDCD')

#initializing the labels (1 for age and 1 for sex)

label1=Label(top,background="#CDCDCD",font=('arial',15,"bold"))
label2=Label(top,background="#CDCDCD",font=('arial',15,"bold"))
sign_image=Label(top)

# function to defining Defect function which detect age and gender of person
#using the model
def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48))  # Correct resizing dimensions
    image = np.array(image)  # Convert to numpy array
    image = np.expand_dims(image, axis=0)  # Expand dimensions to match model input

    sex_f = ['Male', 'Female']
    image = image / 255.0  # Normalize the image

    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))

    print("Predicted age:", str(age))
    print("Predicted gender:", sex_f[sex])
    
    label1.configure(foreground='#011638', text="Age: " + str(age))
    label2.configure(foreground='#011638', text="Gender: " + sex_f[sex])

#defining show_detect botton function
def show_detect_button(file_path):
    Detect_b=Button(top,text='detect image',command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background='#364156',foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46)

#defining the upload image faiqion
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(file_path)
    except:
        pass

upload=Button(top,text='Upload an Image',command=upload_image,padx=10,pady=5)
upload.configure(background='#364156',foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50,)
sign_image.pack(side='bottom',expand=True)

label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
heading=Label(top,text="Age and gender detector",pady=20,font=('arial',20,'bold'))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()



