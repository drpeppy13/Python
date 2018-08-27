mixed_list = ["peanut", "butter", 24, "time"]
integer_list = [0,1,2,3,4,5]
string_list = ["snoop","doggy","dogg"]

def identify_type(list):
    new_string = ""
    total = 0

    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value
    
    if new_string and total:
        print "The array you entered is of mixed type"
        print "String", new_string
        print "Total", total
    
    elif new_string:
        print "The array you entered is of string type"
        print "String", new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total", total

print identify_type(mixed_list)
print identify_type(integer_list)
print identify_type(string_list)