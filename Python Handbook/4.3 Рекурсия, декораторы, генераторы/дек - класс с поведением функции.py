"""
Кэширование. Создание класса с поведением функции
"""

class FuncCreator():
    def __init__(self, start_state):
        self.state = start_state

    def __call__(self):
        print(self.state)
        self.state += 1


func6 = FuncCreator(0)
print(func6.state)  # 0
func6()             # 0
print(func6.state)  # 1