from tkinter import *

root = Tk()
root.title("Discount App")
root.geometry("500x500")
root.config(bg = "lightblue")

def savedA():

    oP = int(origPriceE.get())
    Dis = int(discountE.get())


    amountSaved =  oP * (Dis/100)
    savedE.config(text = amountSaved)
    

    finalPrice = oP - amountSaved
    finalPE.config(text = finalPrice)

origPrice = Label(root, text = "Original Price")
origPrice.grid(row = 0, column = 0, pady = 15)

origPriceE = Entry(root, width = 20)
origPriceE.grid(row = 0, column = 1, padx = 15)

discount = Label(root, text = "Discount (%)")
discount.grid(row = 1, column = 0)

discountE = Entry(root, width = 20)
discountE.grid(row = 1, column = 1, padx = 15)

calculate = Button(root, text = "Calculate", bg = "lightgreen", command = savedA)
calculate.grid(row = 2, column = 1, pady = 20)

saved = Label(root, text = "Amount Saved")
saved.grid(row = 3, column = 0, pady = 15)

savedE = Label(root, width = 20)
savedE.grid(row = 3, column = 1, padx = 15)

finalP = Label(root, text = "Final Price")
finalP.grid(row = 4, column = 0, pady = 15)

finalPE = Label(root, width = 20)
finalPE.grid(row = 4, column = 1, padx = 15)











root.mainloop()