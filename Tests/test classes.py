class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '              
               f'возраст: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())

test_old_none_programmer = Contact('Пушкин', 1799, False)
test_young_programmer = Contact('Ivan', 1986, True)
test_oldschool_none_programmer = Contact('Mitnik', 1975, False)

assert test_young_programmer.is_programmer == True, (
    'Неверный атрибут self.is_programmer'
)
assert test_old_none_programmer.is_programmer == False, (
    'Неверный атрибут self.is_programmer'
)


assert test_old_none_programmer.age_define() == 'Старейшина', (
    'Не работает метод age_define'
)
assert test_young_programmer.age_define() == 'Молодой', (
    'Не работает метод age_define'
)
assert test_oldschool_none_programmer.age_define() == 'Олдскул', (
    'Не работает метод age_define'
)

# Создайте экземпляр класса Contact с необходимыми параметрами
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
# Напишите assert, и в нём проверьте,
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный"
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина"

# Затем создайте другой экземпляр с другими параметрами
# И в assert проверьте, вернут ли и его методы ожидаемый результат.

# Создайте столько экземпляров, сколько нужно,
# чтобы через разные assert проверить все методы во всех вариантах.