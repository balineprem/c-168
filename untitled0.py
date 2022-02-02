class Citizen:
    
    def __init__(self, name, age, dob, id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name:" + self.citizen_name)
        print("Age:" +str (self.citizen_age))
        print("DOB:" + self.citizen_dob)
        print("Citizen Id:" + self.citizen_id)
        print("Citizen Added")

citizen1 = Citizen("Anu", 9,"5th may 2012", "0199")
citizen1.add_citizen() 

citizen2 = Citizen("Sragvi", 11,"17th November 2010", "0198")
citizen2.add_citizen()
       