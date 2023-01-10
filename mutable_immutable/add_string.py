def add_str(string):
    string+='world'

input_str=input()
add_str(input_str)

print(input_str)

----------------------------------

def add_str(string):
    string+='world'
    return string

input_str=input()
input_str=add_str(input_str)

print(input_str)
