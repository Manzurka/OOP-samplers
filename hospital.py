class Patient(object):
    def __init__(self, ID, name, allergies):
        self.id=ID
        self.name=name
        self.allergies=allergies
        self.bed_number=None
       
class Hospital(Patient):
    bed_number=0
    def __init__(self, ID, name, allergies):
        super(Hospital, self).__init__(ID, name, allergies)
        self.patient = ID, name, allergies
        Hospital.list = list()
        Hospital.capacity = 1000
        Hospital.occupancy=len(Hospital.list)

    def admit(self):
        if Hospital.occupancy<=Hospital.capacity:
            Hospital.list.append(self.patient)
            Hospital.bed_number+=1
            Hospital.capacity-=1
        return "{} is admitted.\nHospital capacity:{} \nHospital log:{}".format(self.name,Hospital.capacity,Hospital.list)

    def discharge(self):
        # for self.patient in Hospital.list:
        #     if self.patient[1] == name:
                Hospital.list.remove(self.patient)
                Hospital.bed_number-=1
                Hospital.capacity+=1
                return  "{} is discharged.\nHospital capacity:{} \nHospital log:{}".format(self.name,Hospital.capacity,Hospital.list)

    def info(self):
        return "Patient information: \nID: {} \nName: {} \nAllergies: {} \nBed Number: {}".format(self.id, self.name, self.allergies,Hospital.bed_number)
        

p1=Hospital("77658001","Mike Smith","dairy")
p2=Hospital("77658002","Jenny Walker","aspirin")
p3=Hospital("77658003","Rob Jackson","none")

print p1.admit()
print p1.info()
print p2.admit()
print p2.info()
print p3.admit()
print p3.info()
print p3.discharge()
print p2.discharge()
