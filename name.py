# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for i in range (0, 4):
#     first_name = students[i]['first_name'] 
#     last_name = students[i]['last_name']
#     # full_name = "first_name", "last_name"
# print first_name, last_name

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }    
print "Students"
for i in range (0, 4):
    print i + 1 , '-' , users['Students'][i]['first_name'], users['Students'][i]['last_name'] , '-' , len(users['Students'][i]['first_name']+users['Students'][i]['last_name'])
print "Instructors"
for i in range (0, 2):
    print i + 1 , '-' , users['Instructors'][i]['first_name'], users['Instructors'][i]['last_name'] , '-' , len(users['Instructors'][i]['first_name']+users['Instructors'][i]['last_name'])

print "******************"
test = users['Students']
first_record = test[0]
fName = first_record['first_name']
print fName