from model import Person

class PersonDal: 
  @classmethod
  def save(cls, person: Person):
    with open('person.txt' 'w') as arq: 
      arq.write(person.name + " " + str(person.age) + " " + person.id)
  
  @classmethod
  def read(self): 
    name = 'sergio'
    age = 40
    id = 744997
    return Person(name, age, id)


p1 = Person('Sergio', 40, '74748499040')
print(PersonDal.read().id)