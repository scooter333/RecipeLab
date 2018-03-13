from constants import *
import re
import random


def fry2bake(ingredientList, preparationList):
    print (ingredientList)
    # print (preparationList)

    step1 = "Preheat the oven for 10 min"
    new_prep_list = [step1]
    for step in preparationList:
        new_step = step
        for key in fry2bakeMethods.keys():
            if key in new_step:
                print (key)
                new_step = new_step.replace(key, fry2bakeMethods[key])
                print (new_step)

        new_prep_list.append(new_step)

    # print (new_prep_list)
    return new_prep_list

    #incre ase the time of cooking


def bake2fry(ingredientList, preparationList):
    new_prep_list =[]
    # remove preheat oven line
    # reduce time
    
    return new_prep_list