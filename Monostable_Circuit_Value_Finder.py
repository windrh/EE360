def suffix(num):
    suffixes = [' ', 'K', 'M', 'B', 'T', 'P', 'E', 'Z', 'Y']
    decimal_suffixes = ['', 'm', 'µ', 'n', 'p', 'f', 'a', 'z', 'y']
    sign = '-' if num < 0 else ''
    num = abs(num)
    suffix_idx = 0
    while num >= 1000.0 and suffix_idx < len(suffixes) - 1:
        num /= 1000.0
        suffix_idx += 1
    if suffix_idx == 0:
        return f"{sign}{num:.1f}{decimal_suffixes[0]}{suffixes[0]}"
    decimal_idx = 0
    while num < 1.0 and decimal_idx < len(decimal_suffixes) - 1:
        num *= 1000.0
        decimal_idx += 1
    return f"{sign}{num:.1f}{decimal_suffixes[decimal_idx]}{suffixes[suffix_idx]}"

def capacsuffix(num):
    initialnum = num
    count = 0
    while num < 1:
        num = num * 10
        count += 1
    if count == 4:
        return str(num*100) + "u"
    elif count == 5:
        return str(num*10) + "u"
    elif count == 6:
        return str(num) + "u"
    elif count == 7:
        return str(num*100) + "n"
    elif count == 8:
        return str(num*10) + "n"
    elif count == 9:
        return str(num) + "n"
    else:
        return str(initialnum)

def finder():
    a = open("C:\\Users\\william.hoffman\\PycharmProjects\\AY23\\testdata.txt", "r")
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
                print("\nCapacitor: " + capacsuffix(element) + " Farads" + "\nResistor: " + str(suffix(element2)) + " Ohms")

    booll = False
    while not booll:
        inu = input("\nPress 'q' to close, 'r' to restart program")
        if inu == 'q':
            return 0
        if inu == 'r':
             if finder() == 0:
                 return None

finder()

