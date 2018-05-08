students = [
    {"first_name": "Michael", "last_name" : "Jordan"},
    {"first_name": "John", "last_name" : "Rosales"},
    {"first_name": "Mark", "last_name" : "Guillen"},
    {"first_name": "KB", "last_name" : "Tonel"},
]
users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def show_pupils(arr):
    for pupil in students: 
        print pupil["first_name"], pupil["last_name"]
def show_online(users):
    for role in users:
        counter = 0
        print role
        for someone in users[role]:
            counter +=1
            first_name = someone["first_name"].upper()
            last_name = someone["last_name"].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)
show_pupils(students)
show_online(users)