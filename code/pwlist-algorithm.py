# Version 0.3
from algorithm_data import *
from user_inputs import *
print("*** PWLIST-ALGORITHM BY Opensourcehack3rs ***")
print("*** STARTING ***")

standard_info = user_inp_information()
length_limit = pw_len_limit()
base_list = string_filtering(standard_info)
data_processing(base_list, length_limit)
print("*** WORDLIST CREATED ***")

