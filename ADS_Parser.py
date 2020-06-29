import sys

print("Enter string, press 'ctrl+d' when done to input")
user_input = str(sys.stdin.readlines())  # Reads multi-line string input

user_input = (user_input.split(",")) # Turns string into list of strings at the ','


formatted_user_input_list = []
formatted_user_input_str = ""
for line in user_input: # Iterates over each string in the list and then adds them to a complete formatted string
    line = line.split("INF:     ")[1]
    line = line.replace("20", "b")
    line = line.replace("\\n'", "")
    line = line.replace("20", "b")
    line = line.replace(" ", "")
    print(line)
    formatted_user_input_str += line

print(formatted_user_input_str)

standard_map = formatted_user_input_str[:53]
formatted_user_input_str = formatted_user_input_str[53:]
print(standard_map)
print(formatted_user_input_str)