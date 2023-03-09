class Cat:
    def __init__(self, name='', gender='', age=''):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict): # инициализация объекта
        self.name = cat_dict['name']
        self.gender = cat_dict['gender']['name']
        self.age = cat_dict["age"]