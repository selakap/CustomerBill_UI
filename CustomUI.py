
from tkinter import *

root = Tk()
DiscountAmout = 0
BillAmount = 0


def getSquareRoot ():

    label1 = Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)

def getBill ():
    if (len(customerBillEntry.get()) != 0) and (len(itemCodeEntry.get()) != 0) and (len(descriptionEntry.get()) != 0) and (len(itemPriceEntry.get()) != 0) and (len(noOfItemsEntry.get()) != 0):
        global BillAmount, DiscountAmout, billAmountL, DiscountL

        x = itemPriceEntry.get()
        y = noOfItemsEntry.get()
        BillAmount = float(x)*float(y)
        billAmountL = Label(root, text= BillAmount)
        billAmountL.pack()
        canvas1.create_window(500, 300, window=billAmountL)
        if (2500 <= BillAmount < 5000):
            DiscountL = Label(root, text= "5%")
            DiscountAmout = 5
        elif (5000 <= BillAmount < 7500):
            DiscountL = Label(root, text= "10%")
            DiscountAmout = 10
        elif (7500 <= BillAmount < 10000):
            DiscountL = Label(root, text= "12%")
            DiscountAmout = 12
        elif (1000 <= BillAmount < 15000):
            DiscountL = Label(root, text= "15%")
            DiscountAmout = 15
        elif (15000 <= BillAmount < 20000):
            DiscountL = Label(root, text= "20%")
            DiscountAmout = 20
        elif (BillAmount >= 20000):
            DiscountL = Label(root, text= "25%")
            DiscountAmout = 25
        else:
            DiscountL = Label(root, text= "0%")
            DiscountAmout = 0
        DiscountL.pack()
        canvas1.create_window(500, 350, window=DiscountL)

def getBalance ():
    global balanceL
    if (len(customerBillEntry.get()) != 0) and (len(itemCodeEntry.get()) != 0) and (len(descriptionEntry.get()) != 0) and (len(itemPriceEntry.get()) != 0) and (len(itemPriceEntry.get()) != 0) and (len(givenEntry.get()) != 0):
        GivenAmount = givenEntry.get()
        if DiscountAmout > 0:
            Balance = float(GivenAmount) + ((float(BillAmount) * float(DiscountAmout))/100) - float(BillAmount)
        else:
            Balance = float(GivenAmount) - float(BillAmount)
        balanceL = Label(root, text=Balance)
        balanceL.pack()
        canvas1.create_window(500, 450, window=balanceL)

def clear ():
    customerBillEntry.delete(0, 'end')
    itemCodeEntry.delete(0, 'end')
    descriptionEntry.delete(0, 'end')
    itemPriceEntry.delete(0, 'end')
    noOfItemsEntry.delete(0, 'end')
    givenEntry.delete(0, 'end')
    balanceL.config(text="")
    DiscountL.config(text="")
    billAmountL.config(text="")



####################################################################################

canvas1 = Canvas(root, width = 600, height = 700)

####################################################################################


customerBillLabel = Label(root, text='Customer Bill')
customerBillLabel.config(font=('Arial', 15))
canvas1.create_window(100, 25, window=customerBillLabel)

customerBillEntry = Entry (root)
canvas1.create_window(500, 25, window=customerBillEntry)

#######################################################################

itemCodeLabel = Label(root, text='Item Code')
itemCodeLabel.config(font=('Arial', 10))
canvas1.create_window(100, 100, window=itemCodeLabel)

itemCodeEntry = Entry (root)
canvas1.create_window(500, 100, window=itemCodeEntry)

#######################################################################

descriptionLabel = Label(root, text='Descrition')
descriptionLabel.config(font=('Arial', 10))
canvas1.create_window(100, 150, window=descriptionLabel)

descriptionEntry = Entry (root)
canvas1.create_window(500, 150, window=descriptionEntry)

########################################################################

itemPriceLabel = Label(root, text='Item Price')
itemPriceLabel.config(font=('Arial', 10))
canvas1.create_window(100, 200, window=itemPriceLabel)

itemPriceEntry = Entry (root)
canvas1.create_window(500, 200, window=itemPriceEntry)

####################################################################

noOfItemsLabel = Label(root, text='No of Items')
noOfItemsLabel.config(font=('Arial', 10))
canvas1.create_window(100, 250, window=noOfItemsLabel)

noOfItemsEntry = Entry (root)
canvas1.create_window(500, 250, window=noOfItemsEntry)

#####################################################################

billAmountLabel = Label(root, text='Bill Amount')
billAmountLabel.config(font=('Arial', 10))
canvas1.create_window(100, 300, window=billAmountLabel)

#billAmountEntry = Entry (root)
#canvas1.create_window(500, 300, window=billAmountEntry)

####################################################################

discountLabel = Label(root, text='Discount')
discountLabel.config(font=('Arial', 10))
canvas1.create_window(200, 350, window=discountLabel)


##########################################################################

givenLabel = Label(root, text='Given')
givenLabel.config(font=('Arial', 10))
canvas1.create_window(100, 400, window=givenLabel)

givenEntry = Entry (root)
canvas1.create_window(500, 400, window=givenEntry)

######################################################################

BalanceLabel = Label(root, text='Balance')
BalanceLabel.config(font=('Arial', 10))
canvas1.create_window(250, 450, window=BalanceLabel)


#################################################################

billButton = Button(text='Bill', command=getBill)
canvas1.create_window(100, 500, window=billButton)

#####################################################################

balanceButton = Button(text='Balance', command=getBalance)
canvas1.create_window(300, 500, window=balanceButton)


##############################################################

clearButton = Button(text='Clear', command=clear)
canvas1.create_window(450, 500, window=clearButton)


canvas1.pack()


root.mainloop()
