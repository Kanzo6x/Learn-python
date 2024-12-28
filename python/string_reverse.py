
#slicing syntax method (1)
#str[start:stop:step]
str = "AMRNASER"
print(str[::-1])


#RECURSION  (2)
def string_reversel(str):
    if len(str) == 0:
        return str
    else:
        return string_reversel(str[1:]) + str[0]
    
print(string_reversel("kanzoIsHere"))