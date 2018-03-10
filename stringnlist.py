words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day", "month")

myList = [2,54,-2,7,12,98]
print max(myList)
print min(myList)

x = ["hello",2,54,-2,0.5,7,12,98,"world"]
print x[0::len(x)-1]     #prints the first and last item :: skips numbers in between
print x[0], x[-1]        #prints first and last item of list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()                 #sorts list x smallest to biggest
y = x[:len(x)/2]         #assigns first half of list split by total length of list
z = x[len(x)/2:]         #assigns second half of list split by total length of list
newList = y, z           #assign y and z to a variable so it can be printed at the same time
print newList