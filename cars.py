class Backpack:

    def __init__(self):
        self.content = []

    def add(self, costom):
        self.content.append(costom)
        print("Добавим", costom)

    def __str__(self):
        return 'В рюкзаке ' + ', '.join(self.content)

    def __len__(self):
        len(self.content)

    def __bool__(self):
        return self.content != 0

my_backpack = Backpack()
girls_backpack = Backpack()

if not my_backpack:
    print(my_backpack)
else:
    print('Нічога немя!')

if not girls_backpack:
    print(girls_backpack)
else:
    print('Нічога немя!')

my_backpack.add('Водка')
girls_backpack.add('Презики')

if my_backpack:
    print(my_backpack)
else:
    print('Нічога немя!')

if girls_backpack:
    print(girls_backpack)
else:
    print('Нічога немя!')


