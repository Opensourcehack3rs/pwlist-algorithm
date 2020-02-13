# Version 0.3
def pw_len_limit():
    length_limit = input("PLEASE ENTER THE MAXIMUM LENGTH FOR THE PASSWORDS GETTING GENERATED | FOR NO LIMIT ENTER 0:  ")
    return length_limit

def user_inp_information():
    print("*** INFORMATION SPIDER FOR GENERATING THE PASSWORD-LIST ***")
    print("*** ENTER DATES IN THIS FORMAT DD/MM/YYYY ***")
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
    x = 1
    if standard_info["Loved"] == "none":
        pass
    else:
        standard_info["Loved-nickname"] = input("NICKNAME OF WIFE/GIRLFRIEND | HUSBAND/Boyfriend | IF NOT EXISTENT ENTER NONE: ")
        standard_info["Loved-birthday"] = input("BIRTHDAY OF THE SIGNIFICANT OTHER: ")

    info2 = int(input("NUMBER OF CHILDREN: "))
    x = 1
    while info2 > 0:
        standard_info["chilren-name-" + str(x)] = input("NAME OF CHILD " + str(x) + ": ")
        standard_info["children-nickname-" + str(x)] = input("NICKNAME OF CHILD " + str(x) + ": ")
        standard_info["children-birthday-" + str(x)] = input("CHILD'S " + str(x) + " DATE OF BIRTH: ")
        x = x + 1
        info2 = info2 -1
    standard_info["fav-number"] = input("FAVOURITE NUMBER | IF NOT EXISTENT ENTER: none ")
    standard_info["gamertag/nickname"]=input("GAMERTAG OR NICKNAME | IF NOT EXISTENT ENTER: none ")

    return standard_info

def user_inp_add_information():
    q1 = input("ANY ADDITIONAL INFORMATION TO ADD: Y | N: ")
    if q1 == "N":
        addi_info = 0
    if q1 == "Y":
        addi_info  = []
        print("PLEASE ENTER DATES IN THE FORMAT: DD/MM/YYYY START WITH A HASHTAG #DD/MM/YYYY")
        print("DO NOT USE ANY SPECIAL SIGNS EXCEPT THE # ")
        print("TO STOP THE QUESTIONS ENTER none")
        x = 1
        while x != 0:
            add = input("INFORMATION " + str(x) + ": ")
            if add == "none":
                x = 0
            else:
                addi_info.append(add)
                x = x + 1
    return addi_info



