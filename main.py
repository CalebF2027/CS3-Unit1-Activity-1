def bake_cookies():
        print("Put the ingredients in a bowl.")
        print("Put the cookies in the oven.")
        print("Enjoy the cookies!")

def welcome_message():
      print("Welcome to my kitchen!")
      print("Today we will be making cookies!")

def list_ingredients(main_ingredient, side_ingredient):
      print(f"Main Ingredient: {main_ingredient}")
      print(f"Side Ingredient: {side_ingredient}")

def make_cookies(ingredient1, ingredient2):
      return f"{ingredient1} and {ingredient2} Surprise!"

def add_spice(cookies, spice="cinnamon"):
      print(f"Adding a dash of {spice} to the {cookies}. Yum!")

def cook_recipe():
    welcome_message()
    bake_cookies()
    list_ingredients("flour", "sugar")
    cookies = make_cookies("Chocolate Chip", "Cookies")
    print("Dish made: ", cookies)
    add_spice(cookies)
def main():
      cook_recipe()


if __name__ == "__main__":
    main()
