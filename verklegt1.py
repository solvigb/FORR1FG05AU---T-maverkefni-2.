ekki = "j"
while ekki == "j":
    tala = int(input("Sláðu inn sentimetera"))
    metrar = tala / 100 
    cm = tala % 100
    print(round(metrar), "metrar")
    print(round(cm), "cm")
    ekki = input("Viltu keyra forrit aftur? Sláðu inn j ef já")
    

