# Version 0.2
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
    file = open("pwlist-created-wordlist.txt", "a")
    for i in range(1,len(base_list)+1):
        drip = [list(x) for x in itertools.permutations(base_list, i)]
        end_list.extend(drip)
    for element in end_list:
        string = ''.join(element)
        if len(string) <= 12:
            file.write(string + "\n")
        else:
            pass
    file.close()