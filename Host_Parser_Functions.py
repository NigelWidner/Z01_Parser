
def chosen_host_func():
    host_select_dict = {
        "1": "Heartland",
        "2": "ATL",
        "3": "NBS",
        "4": "RBS",
    }

    print('''
    Please make a select a host!
(1): Heartland
(2): ATL
(3): NBS
(4): RBS
    ''')
    selection = input(">")
    chosen_host = host_select_dict.get(selection, "An invalid selection")
    return chosen_host
    # print(f"You chose {chosen_host}")
    # return chosen_host # I think return provides a value back to what calls the function


