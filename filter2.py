sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = (12, 13)
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
 
current_tester = lL
current_type = type(current_tester)
if current_type is int:
    if current_tester >= 100:
        print "That's a big number!"
    else:
        print "That's a small number!"
elif current_type is str:
    if len(current_tester) >= 20:
        print "Long sentence!"
    else:
        print "Short sentence!"
elif current_type is list:
    if len(current_tester) >= 10:
        print "That's a Long list!"
    else:
        print "What a s Short List!"