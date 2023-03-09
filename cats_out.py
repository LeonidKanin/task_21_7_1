import requests
from cat import Cat
"""
Получение данных об имеющихся котах на сайте "Дом питомца".
"""
cats = requests.get("http://158.160.56.133/api/pet/?page=1&page_size=6&species__name=кошка").json()["results"]

"""
Вывод данных об имеющихся котах с помощью метода init_from_dict(), определенного в классе Cat.
"""
for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(f"Найдена кошка по имени {cat_obj.name}, пол - {cat_obj.gender}, возраст - {cat_obj.age} год(а).")