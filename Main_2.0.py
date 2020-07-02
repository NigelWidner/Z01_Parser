import sys

print("Enter string, press 'ctrl+d' when done to input")
user_Input = str(sys.stdin.readlines())  # Reads multi-line string input and assigns to variable
print(user_Input)
print("~-~-~-~-~-~-~")

user_Input = user_Input.split(",")
print(user_Input)

user_Input_Combined = ''
for user_Input_String in user_Input:
    user_Input_String = user_Input_String.partition("INF:      ")[2]
    user_Input_String = user_Input_String.partition("\\n'")[0]
    user_Input_String = user_Input_String.replace("'", "")
    user_Input_String = user_Input_String.replace("]", "")
    user_Input_Combined += user_Input_String + " "

user_Input_Combined = user_Input_Combined.replace("  ", " ")
user_Input_List = user_Input_Combined.split(" ")
print(user_Input_List)

