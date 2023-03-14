def finder():
    a = open("stdvalue.txt", "r")
    error = float(input("Please enter the margin of error you would like to have: "))
    b = a.read()
    a.close()
    Ohms_Resistor_String = b.split(":")[0]
    Farad_Capacitor_String = b.split(":")[1]
    standard_resistor_value_list_str = Ohms_Resistor_String.split(" ")
    standard_capacitor_value_list_str = Farad_Capacitor_String.split(" ")
    standard_resistor_value_list = []
    standard_capacitor_value_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in standard_resistor_value_list_str:
        if item != '':
            numbercollector = ''
            suffixbool = ''
            for ascii in item:
                if alphabet.find(ascii) > -1:
                     suffixbool += ascii
                elif alphabet.find(ascii) == -1:
                    numbercollector += ascii
            if suffixbool != '':
                if suffixbool == "K":
                    standard_resistor_value_list.append(float(numbercollector) * 1000)
                elif suffixbool == "M":
                    standard_resistor_value_list.append(float(numbercollector) * 1000000)
            else:
                standard_resistor_value_list.append(float(numbercollector))

    for item in standard_capacitor_value_list_str:
        if item != '':
            numbercollector = ''
            suffixbool = ''
            for ascii in item:
                if alphabet.find(ascii) > -1:
                     suffixbool += ascii
                elif alphabet.find(ascii) == -1:
                    numbercollector += ascii
            if suffixbool != '':
                if suffixbool == "p":
                    standard_capacitor_value_list.append(float(numbercollector) * (10 ** -12))
                elif suffixbool == "n":
                    standard_capacitor_value_list.append(float(numbercollector) * (10 ** -9))
                elif suffixbool == "u":
                    standard_capacitor_value_list.append(float(numbercollector) * (10 ** -6))
                elif suffixbool == "m":
                    standard_capacitor_value_list.append(float(numbercollector) * (10 ** -3))

            else:
                standard_capacitor_value_list.append(float(numbercollector))

    desired_input = float(input("What time interval are you looking for (seconds)?  "))

    def isclose(number, desired_input, acceptable_error):
        low_range = (1 - acceptable_error) * desired_input
        high_range = (1 + acceptable_error) * desired_input
        if low_range <= number <= high_range:
            return True
        else:
            return False

    for element in standard_capacitor_value_list:
        for element2 in standard_resistor_value_list:
            if isclose((element * element2 * 1.1),desired_input,error) == True:
                print("\nCapacitor: " + str(element) + "\nResistor: " + str(element2))

    booll = False
    while not booll:
        inu = input("Press 'q' to close, r to restart program")
        if inu == 'q':
            return 0
        if inu == 'r':
             if finder() == 0:
                 return None

finder()
