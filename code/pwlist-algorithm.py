# Version 0.2
from algorithm_data import *
from user_inputs import *
print("*** PWLIST-ALGORITHM BY Opensourcehack3rs ***")
print("*** STARTING ***")

standard_info = user_inp_information()
base_list = string_filtering(standard_info)
data_processing(base_list)
print("*** WORDLIST CREATED ***")

