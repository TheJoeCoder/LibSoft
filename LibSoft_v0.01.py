from guipro import alerts, App, Box, CheckBox, Combo, MenuBar, Picture, PushButton, RadioButton, Slider, Text, TextBox, yesno, info

def TextOnly():
    StartChoice = input("Please Choose From One of the Following: View (V), Create (C) or Loan (L) ")

    if StartChoice == "C":
        filename = input("Enter New Barcode: ")
        file2 = open(filename + '.txt', 'w')
        file = open(filename + '.txt', 'x')
        NameWrite = input("Please Enter the Name of the Person ")
        file.write("NAME: " + NameWrite + '\n')
        file.close()
        file2.close()
        print("[INFO] Account Created!")

    if StartChoice == "L":
        filename = input("Enter Barcode of Person ")
        file = open(filename + '.txt', 'w')
        barcodeWrite = input("Please Enter The Book Number/Barcode")
        file.write(barcodeWrite + '\n')
        file.close()
        print("[INFO] Added Loan!")

    if StartChoice == "V":
        filename = input("Enter Barcode of Person ")
        file = open(filename + '.txt', 'r')
        file.readlines()
        file.close()

def create():
    filename = input("Enter New Barcode: ")
    file = open(filename + '.txt', 'x')
    file2 = open(filename + '.txt', 'w')
    NameWrite = input("Please Enter the Name of the Person ")
    file.write("NAME: " + NameWrite + '\n')
    file.close()
    file2.close()
    print("[INFO] Account Created!")

def loan():
    filename = input("Enter Barcode of Person ")
    file = open(filename + '.txt', 'w')
    barcodeWrite = input("Please Enter The Book Number/Barcode")
    file.write(barcodeWrite + '\n')
    file.close()
    print("[INFO] Added Loan!")

def view():
    filename = input("Enter Barcode of Person ")
    file = open(filename + '.txt', 'r')
    file.readlines()
    file.close()



choosemethod = App(title="Choose Option", width=300, height=200)
button1 = PushButton(choosemethod, command=TextOnly, text="Start With Text")
button2 = PushButton(choosemethod, command=create, text="Create Account")
button3 = PushButton(choosemethod, command=loan, text="Add A Book To The Account")
button4 = PushButton(choosemethod, command=view, text="View The Book(s) On The Account")
choosemethod.display()
