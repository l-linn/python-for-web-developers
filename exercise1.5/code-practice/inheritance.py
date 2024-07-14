class Person(object):
  def walk():
    print('I can walk')

class Tom(Person):
  def talk():
    print('I can talk')

print(Tom.talk())
print(Tom.walk())

class Animal(object):
  #Every animal has an age, but a name may not be necessary
  def __init__(self, age):
    self.age = age
    self.name = None
  #getter methods    
  def get_age(self):
    return self.age
  def get_name(self):
    return self.name
  #setter methods
  def set_age(self, age):
    self.age = age
  def set_name(self, name):
    self.name = name
  #string representation
  def __str__(self):
    output = "\nClass: Animal\nName: " + str(self.name) + \
      "\nAge: " + str(self.age)
    return output

animal = Animal(2)
print(animal)
