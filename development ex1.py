#Aaron Bentley
#development exercise 1
import pickle

class Birth_record:
    def __init__(self):
        self.Name = None
        self.birthdate = None

birthdays = []
for count in range(3):
    birth = Birth_record()
    birth.Name = input("Name: ")
    birth.birthdate = input("Date of Birth: ")
    birthdays.append(birth)

with open("dev2.dat",mode="wb") as my_file:
    pickle.dump(birthdays,my_file)
