class Call(object):
    def __init__(self, u_id, name, phone_number, time, reason):
        self.u_id = u_id
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason
    def display_info(self):
        print "Unique ID: ", self.u_id
        print "Name: ", self.name
        print "Phone Number: ", self.phone_number
        print "Call Time: ", self.time
        print "Call Reason: ", self.reason
class CallCenter(object):
    def __init__()

call1 = Call(1, "Kyle", 5627600484, "8:30pm", "Call Back")

call1.display_info()