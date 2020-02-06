# Version 0.3
def string_filtering(standard_info):
    from copy import deepcopy
    standard_info_copy = deepcopy(standard_info)
    base_list_part = []
    date_list = []
    for key in standard_info_copy:
        if standard_info_copy[key] == "none":
            del standard_info[key]
        else:
            element = str(standard_info[key])
            element = element.replace(".", "")
            element = element.replace(" ", "")
            element = element.replace("/", "")
            if "day" in str(key):
                year = element[-2:]
                date = element[:-4]
                yeardate = date + year
                date_list.append(element)
                date_list.append(year)
                date_list.append(date)
                date_list.append(yeardate)
                date_list.append(element[-4:])
            base_list_part.append(element)
    base_list = base_list_part + date_list
    return base_list


def data_processing(base_list):
    import itertools
    end_list = []
    file = open("pwlist-created-wordlist.txt", "w")
    file.write("")
    file.close()
    for i in range(1, len(base_list) + 1):
        drip = [list(x) for x in itertools.permutations(base_list, i)]
        end_list.extend(drip)
    return end_list

def capital_letters_replacement(end_list):
    big_list = []
    writing_list = []
    chars = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E' 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                    'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r' ,'S', 's', 'T', 't', 'U',
                    'u',
                    'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    for element in end_list:
        string = ''.join(element)
        if len(string ) >= 1:
            if string[0] in chars:
                big_list.append(string.capitalize())
        else:
            pass
    writing_list.extend(end_list)
    for element in big_list:
        string = ''.join(element)
        string = string.replace(string[0], chars[chars.index(string[0])+1])
        writing_list.append(string)
    return writing_list


def writing(writing_list, length_limit):
    file = open("pwlist-created-wordlist.txt", "a")
    if length_limit == "none":
        length_limit = 18
    print("*** WRITING GENERATED PASSWORDS INTO THE WORDLIST ***")
    for element in writing_list:
        string = ''.join(element)
        if len(string) <= int(length_limit):
           file.write(string + "\n")
        else:
            pass
    file.close()