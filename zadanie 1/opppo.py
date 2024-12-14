class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def info(self):
        return f"Info: Name: {self.name}, Color: {self.color}"

class Fish(Animal):
  def __init__(self, name, color, location):
    super().__init__(name, color)
    self.location = location

  def info(self):
    return f"{super().info()}, location: {self.location}"

class Bird(Animal):
  def __init__(self, name, color, max_speed):
    super().__init__(name, color)
    self.max_speed = max_speed

  def info(self):
    return f"{super().info()}, max speed: {self.max_speed}"

class Insect(Animal):
  def __init__(self, name, color, size, date_of_discovery):
    super().__init__(name, color)
    self.size = size
    self.date_of_discovery = date_of_discovery

  def info(self):
    return f"{super().info()}, size: {self.size}, date of discovery: {self.date_of_discovery}"



filename = 'data.txt'
with open(filename, 'r') as file:

  array_of_animal = []

  for line in file:
    if 'ADD' in line:
      family = line.split()[1]
      name = line.split()[2]

      if family == 'Bird':
        max_speed = line.split()[4]
        obj = Bird(name = line.split()[2], color = line.split()[3], max_speed = line.split()[4])

      if family == 'Fish':
        obj = Fish(name = line.split()[2], color = line.split()[3], location = line.split()[4])

      if family == 'Insect':
        obj = Insect(name = line.split()[2], color = line.split()[3], size = line.split()[4], date_of_discovery = line.split()[5])

      array_of_animal.append(obj)

    if 'REM' in line:
      name = line.split()[1]
      for obj in array_of_animal:
        if name == obj.name:
          array_of_animal.remove(obj)

    if 'print' in line:
      for obj in array_of_animal:
        print(obj.info())