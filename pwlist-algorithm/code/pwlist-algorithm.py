# Version 0.3
from algorithm_data import *
from user_inputs import *
print("*** PWLIST-ALGORITHM BY Opensourcehack3rs ***")
print("*** STARTING ***")

standard_info = user_inp_information()
addi_info = user_inp_add_information()
length_limit = pw_len_limit()
base_list = string_filtering(standard_info, addi_info)
end_list = data_processing(base_list,length_limit)
writing_list = capital_letters_replacement(end_list)
writing(writing_list, length_limit)

print("*** WORDLIST CREATED ***")

