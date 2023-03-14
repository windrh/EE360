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

    frequency_input = float(input("What the frequency you are looking for? "))
    duty_cycle_input = float(input("What is the duty cycle % you are looking for? ")) * .01

    def istrue(ds,fq,error):
        if (duty_cycle_input * (1 - error)) <= ds <= (duty_cycle_input * (error + 1)) and (frequency_input * (1-error)) <= fq <= (frequency_input*(1+error)):
            return True
        else:
            return False


    for capacitor in standard_capacitor_value_list:
        for resistor1 in standard_resistor_value_list:
            for resistor2 in standard_resistor_value_list:
                T1 = .693 * (resistor1 + resistor2) * capacitor
                T2 = .693 * resistor2 * capacitor
                T = T1 + T2
                duty_cycle = T1/T
                frequency = 1/T
                if istrue(duty_cycle,frequency,error) == True:
                    print("\nCapacitor: " + str(capacitor) + " F" + "\nResistor 1: " + str(resistor1) + " Ohms\nResistor 2: " + str(resistor2) + " Ohms")

    booll = False
    while not booll:
        inu = input("Press 'q' to close, r to restart program")
        if inu == 'q':
            return 0
        if inu == 'r':
             if finder() == 0:
                 return None

finder()
