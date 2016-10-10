
class Car(object):
  """The Car class"""
 
  num_of_doors = 4
  num_of_wheels = 4
  speed = 0
  
  def __init__(self, name='General', model='GM', car_type='saloon'):
    self.name = name
    self.model = model
    self.car_type = car_type
    
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    elif self.car_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_doors
    
  def drive(self,speed):
    """check the speed of vehicle"""
    if self.car_type == 'trailer':
     self.speed = speed * 11
    else:
     self.speed = 10 ** speed    
    return self

  def is_saloon(self):
    """check the type of vehicle"""
    if self.car_type == 'saloon':
      return self.car_type
    elif self.car_type == 'trailer':
      self.car_type = 'trailer'
      return self.car_type
    
opel = Car('Opel', 'Omega 3')
porshe = Car('Porshe', '911 Turbo')

print("The {} car has {} doors and {} wheels ".format(opel.name, opel.num_of_doors,opel.num_of_wheels))
print("The {} car is a {} ".format(opel.name,opel.car_type))
print()
print("The {} car has {} doors and {} wheels ".format(porshe.name, porshe.num_of_doors,porshe.num_of_wheels))
print("The {} car is a {} ".format(porshe.name,porshe.car_type))    
      
  