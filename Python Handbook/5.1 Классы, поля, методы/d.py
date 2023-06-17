

class Programmer():
    POSITIONS = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    def __init__(self, name, position='Junior'):
        self.name = name
        self.position = position
        self.salary = self.POSITIONS[position]
        self.hours = 0
        self.money_earned = 0

    def work(self, time):
        self.hours += time
        self.money_earned += time * self.salary

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
            self.salary = self.POSITIONS[self.position]
        elif self.position == 'Middle':
            self.position = 'Senior'
            self.salary = self.POSITIONS[self.position]
        else:
            self.salary += 1

    def info(self):
        return (f'{self.name} {self.hours}ч. {self.hours} {self.position}  '
                f'{self.money_earned}тгр.)')


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

