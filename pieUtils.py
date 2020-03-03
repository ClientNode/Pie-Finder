import os
from xml.etree import ElementTree
from xml.dom import minidom

filename = 'pieRecipe.xml'
dom = ElementTree.parse(filename)

def getPies(item):
    piesAllowed = list()
    recipes = dom.findall('recipe')
    for r in recipes:
        piename = r.find('pieName').text
        for i in r.findall('ingredient'):
            if item.lower() in i.text.lower():
                if piename not in piesAllowed:
                    piesAllowed.append(piename)
    return piesAllowed

def getPieSteps(pieName):
    steps = list()
    recipes = dom.findall('recipe')
    for r in recipes:
        pie = r.find('pieName').text
        for managesteps in r:
            if pieName.lower() == pie.lower():
                steplist = r.findall('instruction/step')
                for s in steplist:
                    step = s.text
                    if step not in steps:
                        steps.append(step)
    return steps

def getPieIngredients(pieName):
    ingredientList = list()
    recipes = dom.findall('recipe')
    for r in recipes:
        pie = r.find('pieName').text
        if pieName.lower() == pie.lower():
            i = r.find('ingredient')
            for i in r:
                if i.text == pie:
                    continue
                else:
                    ingredientList.append(i.text)
    finalList = [i for i in ingredientList if not i.endswith('\n\t\t\t')]
    return finalList
    


pieInput = input("Enter pie you want to make: ")
ingredientInput = input("Enter ingredient: ")
ingredientInput.lower()
piesAllowed = getPies(ingredientInput)
pieSteps = getPieSteps(pieInput)
pieIngred = getPieIngredients(pieInput)
print()

if len(pieIngred) != 0:
    print("To Make this pie you will need the following ingredients: \n" + "\n".join(pieIngred))
else:
    print("Pie not found...")

if len(pieSteps) != 0:
    print("\nSteps to make the " + pieInput)
    i = 0
    while i < len(pieSteps):
        print("Step", i + 1)
        print(pieSteps[i])
        print("")
        askinput = input("Waiting for command (next, back, repeat): ")
        if askinput == "next":
            i += 1
        elif askinput == "repeat":
            continue
        elif askinput == "back":
            if i != 0:
                i -= 1
        print("")
else:
    print("Pie not found...")

if len(piesAllowed) != 0:
    print("You can make these pies with " + ingredientInput + "(s): " + ", ".join(piesAllowed))
else:
    print("Can't make pies with " + ingredientInput + "!")

