import json
from abc import ABC,abstractmethod
from pathlib import Path

database="school_data.json"
data = {"student" : [], "teachers" : []}

if(Path(database).exists()):
  with open(database,"r") as f:
    content=f.read()
    if(content):
      data=json.loads(content)


def save():
  with open(database,"w") as f:
    json.dump(data,f,indent=4)




class Persons(ABC):

  @abstractmethod
  def get_roles(self):
    pass

  @abstractmethod
  def register(self):
    pass

  @abstractmethod
  def show_details(self):
    pass

  @staticmethod
  def validate_email(email):
    return "@"in email and "." in email






class Student(Persons):

  def get_roles(self):
    return "student"

  def register(self):
    name=input("Tell me your name :-")
    age=int(input("Tell me your age :-"))
    email=input("Tell me your email :-")  
    roll_no=input("Tell me your roll number :-")

    if not Persons.validate_email(email):
      print("Invalid Email")
      return 

    for i in data["student"]:
      if i["roll_no"]== roll_no :
        print("student already exists")
        return 

    data["student"].append({
      "name": name,
      "age" : age,
      "email" : email,
      "roll_no" : roll_no,
      "grades" : {}
    })

    save()

    print(f"student {name} registered successfully.")

  def show_details(self):
    roll_no=input("Tell me your roll number :-")
    for s in data["student"]:
      if s["roll_no"] == roll_no:
        grades=s["grades"]
        avg=sum(grades.values())/len(grades) if grades else 0

        print(f"\n Name :{s['name']}")
        print(f" Roll No :{s['roll_no']}")       
        print(f" Grades :{grades}")
        print(f" Average :{avg:.1f}")
        return



  def add_grades(self):
    roll_no=input("Tell me the roll number :-")
    subject=input("Tell me your subject :- ")
    marks=int(input("Tell me your marks :-"))

    for i in data["student"]:
      if i["roll_no"] ==roll_no:
        i['grades']['subject']=marks
        save()
        print("grade added successfully.")
        return 
    print("Student not found")

class Teacher(Persons):
  def get_roles(self):
    return "Teacher"

  def register(self):
    name=input("Tell me your name :-")
    age=int(input("Tell me your age :-"))
    email=input("Tell me your email :-")  
    emp_id=input("Tell me your emp_id number :-")
    subject=input("Tell me your subject :-")

    if not Persons.validate_email(email):
      print("Invalid Email")
      return 

    for i in data["teachers"]:
      if i["emp_id"]== emp_id :
        print("student already exists")
        return 

    data["teachers"].append({
      "name": name,
      "age" : age,
      "email" : email,
      "emp_id" : emp_id,
      "subject" : subject
    })

    save()
    print(f" Teacher {name} registered successfully.")

  def show_details(self):
      emp_id=input("Tell me your employee id :-")
      for s in data["teachers"]:
        if s["emp_id"] == emp_id:
  
          print(f"\n Name :{s['name']}")
          print(f"Subject : {s['subject']}")
          print(f" Emp Id :{s['emp_id']}")
          return
    

stud = Student() 
tech=Teacher()

print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show a student detail")
print("press 5 to show a teacher detail")

choice =int(input("Please tell your choice :-"))

if(choice==1):
  stud.register()

elif (choice==2):
  tech.register()

elif (choice==3):
  stud.add_grades()

elif(choice==4):
  stud.show_details()

elif(choice==5):
  tech.show_details()