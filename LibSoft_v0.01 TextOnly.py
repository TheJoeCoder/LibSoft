while True:
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
        open(filename + '.txt', 'w')
        barcodeWrite = input("Please Enter The Book Number/Barcode")
        file.write(barcodeWrite + '\n')
        file.close()
        print("[INFO] Added Loan!")

    if StartChoice == "V":
        filename = input("Enter Barcode of Person ")
        file = open(filename + '.txt', 'r')
        file.readlines()
        file.close()


