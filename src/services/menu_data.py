import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.get_dishes(source_path)

    @staticmethod
    def get_dishes(source_path):
        with open(source_path, encoding="utf-8") as file:
            dishes_list = list(csv.reader(file, delimiter=",", quotechar='"'))
            dishes_list.pop(0)

            dishes_set = set()
            for dish in dishes_list:
                dishes_set.add(Dish(dish[0], float(dish[1])))
                for dish_set in dishes_set:
                    if dish_set.name == dish[0]:
                        dish_set.add_ingredient_dependency(
                            Ingredient(dish[2]), int(dish[3]))
            return dishes_set
