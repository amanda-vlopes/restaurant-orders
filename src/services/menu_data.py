import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf-8") as file:
            dishes_list = list(csv.reader(file, delimiter=",", quotechar='"'))
            dishes_list.pop(0)

            dishes_set = set()
            for dish in dishes_list:
                dish_item = Dish(dish[0], float(dish[1]))
                dishes_set.add(dish_item)
                dish_ingredient = Ingredient(dish[2])
                for dish_set in dishes_set:
                    if dish_set.name == dish[0]:
                        dish_set.add_ingredient_dependency(
                            dish_ingredient, int(dish[3]))
            self.dishes = dishes_set
