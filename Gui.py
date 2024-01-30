import pickle
from sklearn import linear_model
import tkinter as tk
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from PIL import Image, ImageTk
from tkinter import messagebox

with open('co2_MLRmodel','rb') as file:
    ourModel1 = pickle.load(file)


with open('co2_Pmodel','rb') as file:
    ourModel2 = pickle.load(file)


root = tk.Tk()
root.geometry("900x700")


def predictMultiLinearRegression():
    global egineSizeEntery, cylinderEntery, fuelConsumptionHwyEntery, fuelConsumptionCityEntery, fuelConsumptionCombEntery1, fuelEntery
    Engine_Size = float(egineSizeEntery.get())
    Cylinders = float(cylinderEntery.get())
    Fuel_Consumption_City = float(fuelConsumptionCityEntery.get())
    Fuel_Consumption_Hwy = float(fuelConsumptionHwyEntery.get())
    Fuel_Consumption_Comb1 = float(fuelConsumptionCombEntery1.get())
    Fuel_Type = float(fuelEntery.get())
    if not (0 <= Fuel_Type < 4):
        messagebox.showerror("Error", "Wrong entered data, try again")
    else:
        print(Fuel_Consumption_Comb1)
        input_data = [[Engine_Size, Cylinders, Fuel_Consumption_City, Fuel_Consumption_Hwy, Fuel_Consumption_Comb1, Fuel_Type]]
        y = ourModel1.predict(input_data)
        messagebox.showinfo("Information", "The predicted value is {}.".format(y))

def predictPolynomialLinearRegression():
    global egineSizeEntery, cylinderEntery, fuelConsumptionHwyEntery, fuelConsumptionCityEntery, fuelConsumptionCombEntery1, fuelEntery
    Engine_Size = float(egineSizeEntery.get())
    Cylinders = float(cylinderEntery.get())
    Fuel_Consumption_City = float(fuelConsumptionCityEntery.get())
    Fuel_Consumption_Hwy = float(fuelConsumptionHwyEntery.get())
    Fuel_Consumption_Comb1 = float(fuelConsumptionCombEntery1.get())
    Fuel_Type = float(fuelEntery.get())
    if not (0 <= Fuel_Type < 4):
        messagebox.showerror("Error", "Wrong entered data, try again")
    else:
        print(Fuel_Consumption_Comb1)
        input_data = [[Engine_Size, Cylinders, Fuel_Consumption_City, Fuel_Consumption_Hwy, Fuel_Consumption_Comb1, Fuel_Type]]
        poly = PolynomialFeatures(degree=3)
        X_predict_poly = poly.fit_transform(input_data)
        y = ourModel2.predict(X_predict_poly)
        messagebox.showinfo("Information", "The predicted value is {}.".format(y))


BG = tk.Label(root, bg="#05003E", height=700, width=800)
BG.place(x=0, y=0)
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()
image = Image.open("co2.jpg")
image = image.resize((600, 300))
background = ImageTk.PhotoImage(image)

canvas.create_image(0, 0, anchor=tk.NW, image=background)

root.title("Co2 Prediction Model")
transparent_image = tk.PhotoImage(width=0, height=0)

headLabel = tk.Label(root, text="Discover the environmental impact of cars through CO2 emissions.", font=("Arial", 15),
                     bg="white")
headLabel.place(x=150, y=5)

makeLabel = tk.Label(root, text="Make", width=11, height=1, font=("Arial", 15), bg="white")
makeLabel.place(x=5, y=330)

makeEntery = tk.Entry(root, width=20)
makeEntery.place(x=150, y=335)

modelLabel = tk.Label(root, text="Model", width=11, height=1, font=("Arial", 15), bg="white")
modelLabel.place(x=5, y=380)

modelEntery = tk.Entry(root, width=20)
modelEntery.place(x=150, y=385)

vechicleLabel = tk.Label(root, text="Vehicle", width=11, height=1, font=("Arial", 15), bg="white")
vechicleLabel.place(x=5, y=430)

vechicleEntery = tk.Entry(root, width=20)
vechicleEntery.place(x=150, y=435)

egineSizeLabel = tk.Label(root, text="Engine size", width=11, height=1, font=("Arial", 15), bg="white")
egineSizeLabel.place(x=5, y=480)

egineSizeEntery = tk.Entry(root, width=20)
egineSizeEntery.place(x=150, y=485)

cylinderLabel = tk.Label(root, text="Cylinder", width=11, height=1, font=("Arial", 15), bg="white")
cylinderLabel.place(x=5, y=530)

cylinderEntery = tk.Entry(root, width=20)
cylinderEntery.place(x=150, y=535)

transmissionLabel = tk.Label(root, text="Transmission", height="1", width="11", font=("Arial", 15), bg="white")
transmissionLabel.place(x=5, y=580)

transmissionEntery = tk.Entry(root, width=20)
transmissionEntery.place(x=150, y=585)

fuelLabel = tk.Label(root, text="Fuel Type", height="1", width="28", font=("Arial", 15), bg="white")
fuelLabel.place(x=350, y=330)

fuelEntery = tk.Entry(root, width=20)
fuelEntery.place(x=700, y=335)

fuelTypeLabel = tk.Label(root, text="Regular gasoline = 0     Premium gasoline = 1     Diesel = 2    Ethanol = 3",
                         height="1", width="55", font=("Arial", 11), bg="white")
fuelTypeLabel.place(x=350, y=370)

fuelConsumptionCityLabel = tk.Label(root, text="Fuel Consumption City", height="1", width="28", font=("Arial", 15),
                                    bg="white")
fuelConsumptionCityLabel.place(x=350, y=430)

fuelConsumptionCityEntery = tk.Entry(root, width=20)
fuelConsumptionCityEntery.place(x=700, y=435)

fuelConsumptionHwyLabel = tk.Label(root, text="Fuel Consumption Hwy", height="1", width="28", font=("Arial", 15),
                                   bg="white")
fuelConsumptionHwyLabel.place(x=350, y=480)

fuelConsumptionHwyEntery = tk.Entry(root, width=20)
fuelConsumptionHwyEntery.place(x=700, y=485)

fuelConsumptionCombLabel1 = tk.Label(root, text="Fuel Consumption Comb(L/100km)", height="1", width="28",
                                     font=("Arial", 15), bg="white")
fuelConsumptionCombLabel1.place(x=350, y=530)

fuelConsumptionCombEntery1 = tk.Entry(root, width=20)
fuelConsumptionCombEntery1.place(x=700, y=535)

fuelConsumptionCombLabel2 = tk.Label(root, text="Fuel Consumption Comb(mpg)", height="1", width="28",
                                     font=("Arial", 15), bg="white")
fuelConsumptionCombLabel2.place(x=350, y=580)

fuelConsumptionCombEntery2 = tk.Entry(root, width=20)
fuelConsumptionCombEntery2.place(x=700, y=585)

predictButton = tk.Button(root, text="Predict MLR Model", height=1, width=15, command=predictMultiLinearRegression)
predictButton.place(x=200, y=650)

predictButton = tk.Button(root, text="Predict P Model", height=1, width=15, command=predictPolynomialLinearRegression)
predictButton.place(x=400, y=650)

root.mainloop()