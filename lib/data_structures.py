spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
"""
def get_names(spicy_foods):
    food_name = []
    for food in spicy_foods:
        food_name.append(food["name"])

    return food_name

print(get_names(spicy_foods))
"""

def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    #return spiciest_food


"""
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cuisine = food.get('cuisine')
        heat_level = food.get('heat_level')
        print(f'{name} ({cuisine}) | Heat Level: {"🌶" * heat_level}')

print_spicy_foods(spicy_foods)

"""

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
        
#print(get_spicy_food_by_cuisine(spicy_foods, "American"))


    
"""      
def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

print_spiciest_foods(spicy_foods)
"""

def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    spiciest_food_print = print_spicy_foods(spiciest_food)
    return spiciest_food_print

#print(print_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    heat_level = sum([food.get("heat_level") for food in spicy_foods])
    average = int(heat_level / len(spicy_foods))
    return average

#print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


