# import Host_Parser_Functions
from Host_Parser_Functions import *
from ADS_Parser import ads_parser

# Prints host select message and prompts for a selection
chosen_host = chosen_host_func()  # How can a function return the value of multiple variables
print(f"You chose {chosen_host}")

if chosen_host == "Heartland":
    ads_parser()
elif chosen_host == "ATL":
    print("ATL")
else:
    print("Uhoh")


