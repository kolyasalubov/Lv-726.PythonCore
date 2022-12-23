ing1 ="tomato"
ing2 = "meat"
ing3 = "salad"
def flag(func):
    def inner(ing1,ing2,ing3):
        print("          ______________")
        print("         / Bon appetit /")
        print("        /_____________/")
        print("       /")
        print("      /")
        func(ing1,ing2,ing3)
    return inner
def buns(func):
    def inner(ing1,ing2,ing3):
        
        print('<\ ^^^^^^^ />')
        func(ing1,ing2,ing3)
        print('<\ ______ />\n')
    return inner
        
def ingridients(func):
    def inner(ing1,ing2,ing3):
        print(f"#{ing1}#")
        print(f"-{ing2}-")
        print(f"~{ing3}~")
    return inner
@flag        
@buns
@ingridients
def sandwich_salad(ing1,ing2,ing3):
    print(f"{ing1} \n{ing2} \n{ing3}")

sandwich_salad(ing1,ing2,ing3)