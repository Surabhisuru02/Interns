class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id,marks=0):
        super().__init__(name, age, gender)                # it will calls the constructor of the (parent class) person to initialize the attributes 
        self.student_id = student_id
        self.marks = marks if marks else {}


    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def calculate_average_marks(self):
        if self.marks:
            average = sum(self.marks.values()) / len(self.marks)
            return average
        else:
            return None


student = Student( "Sahana",20,"Female","4YG21AD045",
                  marks={"CIE-1": 92 ,
                         "CIE-2": 85,
                         "CIE-3": 90,
                         
                         }                    
                  ) 
                    

print("Student Information:")
student.display_student_info()

average_marks = student.calculate_average_marks()
if average_marks:
    print(f"Average Marks: {average_marks:.2f}")
else:
    print("No marks available.")

