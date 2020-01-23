# Version 0.1

def user_inp_information():
    print("*** INFORMATION SPIDER FOR GENERATING THE PASSWORD-LIST ***")
    x = 1
    standard_info = {}
    standard_info["First-Name"] = input("FIRST NAME OF THE TARGET: ")
    standard_info["Second-Name"] = input("MIDDLE NAME OF THE TARGET: ")
    standard_info["Surname"] = input("SURNAME OF THE TARGET: ")
    info1 = int(input("NUMBER OF PETS OWNED BY THE TARGET: "))
    while info1 > 0:
        standard_info["Pet-" + str(x)] = input("NAME OF PET " + str(x) +": ")
        x = x + 1
        info1 = info1 - 1
    standard_info["Place-of-birth"] = input("PLACE OF BIRTH: ")
    standard_info["Birthday"] = input("DATE OF BIRTH: ")
    standard_info["Loved"] = input("NAME OF WIFE/GIRLFRIEND | HUSBAND/BOYFRIEND | IF NOT EXISTENT ENTER: none ")
    info2 = int(input("NUMBER OF CHILDREN: "))
    x = 1
    while info2 > 0:
        standard_info["chilren-name-" + str(x)] = input("NAME OF CHILD" + str(x) + ": ")
        standard_info["children-nickname-" + str(x)] = input("NICKNAME OF CHILD" + str(x) + ": ")
        standard_info["children-birthday-" + str(x)] = input("CHILD'S" + str(x) + "DATE OF BIRTH: ")
        x = x + 1
        info2 = info2 -1
    standard_info["fav-number"] = input("FAVOURITE NUMBER | IF NOT EXISTENT ENTER: none ")
    standard_info["gamertag/nickname"]=input("GAMERTAG OR NICKNAME | IF NOT EXISTENT ENTER: none ")

    return standard_info