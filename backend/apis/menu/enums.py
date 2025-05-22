# models/enums.py

import enum

class CategoryEnum(str, enum.Enum):
    soup = "soup"
    starter = "starter"
    pizza = "pizza"
    burger = "burger"
    noodles = "noodles"
    main_course = "main_course"
    bread = "bread"
    drinks = "drinks"
    dessert = "dessert"
    

class SubCategoryEnum(str, enum.Enum):
    # Meals
    veg = "veg"
    non_veg = "non_veg"
    vegan = "vegan"
    gluten_free = "gluten_free"

    # Drinks
    soft_drink = "soft_drink"
    hot_beverage = "hot_beverage"
    mocktail = "mocktail"
    cocktail = "cocktail"
    alcohol = "alcohol"


class CuisineEnum(str, enum.Enum):
    italian = "italian"
    american = "american"
    indian = "indian"
    chinese = "chinese"
    mexican = "mexican"
    thai = "thai"
    japanese = "japanese"
    mediterranean = "mediterranean"
