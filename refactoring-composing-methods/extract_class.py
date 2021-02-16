# Extract Class

class Recipe:
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe):
        self.name = name 
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = []
        self.recipe = recipe

        for ingredients in recipe:
            self.recipe.append(ingredients)

foods = [Recipe('butternut squash soup', 45, True, 'soup','North African',\
     ['butter squash','onion','carrot', 'garlic','butter','black pepper', 'cinnamon','coconut milk']\
        ,'1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top \
          2. Put all in blender with butter and coconut milk. \
          3. Blend them till they become puree. \
            4. Then move the content into a pot. Add coconut milk. Simmer for 5 mintues.'),

        Recipe('shirazi salad', 5, True, 'salad','Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'], \
            '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 4. add salt'
                '5. Mixed them thoroughly'),

        Recipe('Home-made Beef Sausage', 60, False, 'deli','All',['sausage casing', 'regular ground beef','garlic',\
            'corriander seeds','black pepper seeds','fennel seed','paprika'], \
                '1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                'the seasonings 2. In a bowl, mix ground beef with the'
                'seasoning 3. Add all the content to a sausage stuffer. 4. Put the casing on'
                "the stuffer funnel. 5. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!")]

for recipe in foods:
    print("Name:",recipe.name)
    print("Prep time:",recipe.prep_time, "mins")
    print("Is Veggie?", 'Yes' if recipe.is_veggie else "No")
    print("Food Type:", recipe.food_type)
    print("Cuisine:", recipe.cuisine)
    for item in recipe.ingredients:
        print(item, end=', ')
    print()
    print("recipe", recipe.recipe)
    print("***")
