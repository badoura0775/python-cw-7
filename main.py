class person:
  def __init__(self,name,age):
    self.name= name
    self.age= age
  def __str__(self):
   return f"My name is {self.name} and I am {self.age} years old"
  def is_adult(self):
    if self.age > 18:
        print('You have too much responsibilities')
    else:
        print('Lucky you')

first_person=person("jhon", 22)
print(first_person.name, first_person.age)
print(first_person)
print(first_person.is_adult())