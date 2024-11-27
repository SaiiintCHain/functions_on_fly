from random import choice

#Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_func = list(map(lambda x,u: x == u, first, second))
print(my_func)

#Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                if isinstance(item, str):
                    f.write(item + '\n')
                else:
                    f.write(str(item) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__

class MysticBall:
    def __init__(self, *x):
        self.x = x

    def __call__(self):
        return choice(self.x)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())