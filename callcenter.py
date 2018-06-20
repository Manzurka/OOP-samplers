class Call(object):
    def __init__(self, ID, name, phone, time, reason):
        self.id=ID
        self.name=name
        self.phone=phone
        self.time=time
        self.reason=reason

    def display(self):
        return "Call attributes: \nID: {} \nName: {} \nPhone: {} \nTime: {} \nReason: {}".format(self.id, self.name, self.phone,self.time, self.reason)

class CallCenter(Call):
    def __init__(self, ID, name, phone, time, reason):
        super(CallCenter, self).__init__(ID, name, phone, time, reason)
        self.call = ID, name, phone, time, reason
        CallCenter.list = list()
        self.queue_size= 0

    def add(self):
        CallCenter.list.append(self.call)
        self.queue_size +=1
        return CallCenter.list

    def remove(self):
        CallCenter.list.pop(0)
        self.queue_size -=1
        return CallCenter.list

    def info(self):
        return "Info: \nName: {} \nPhone Number: {} \nQueue: {}".format(self.name,self.phone,self.queue_size)

call1=CallCenter("1","Mike Smith","602-354-6466", "13.30", "Account Closure")
call2=CallCenter("2","Jenny Walker","480-693-9385", "13.45", "Account Issues")
call3=CallCenter("3","Rob Jackson","480-783-2435", "13.48", "Payments")

print call1.add()
print call2.add()
print call3.add()
print call3.remove()
print call2.info()
print call3.display()

