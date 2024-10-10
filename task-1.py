#Task: Create a simple Person class with attributes like name, age, and gender.
#add list of dictionary insted of user input

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display_info(self):
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")
      print(f"Gender: {self.gender}")

def main():
   print("\nYour Information:")
   people_info = [
        {"name": "A", "age": 30, "gender": "Male"},
        {"name": "B", "age": 25, "gender": "Female"},
        {"name": "C", "age": 40, "gender": "Male"},
        {"name": "D", "age": 28, "gender": "Female"}
    ]
   for person_info in people_info:
        
        person = Person(person_info["name"], person_info["age"], person_info["gender"])
        person.display_info()
if __name__ == "__main__":
    main()



HEPL ME
