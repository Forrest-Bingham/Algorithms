#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    print(len(recipe), "-- Recipe ingredients --", len(ingredients))
    at_least_one_batch = True
    max_batches = 0
    loops = 0
    if len(recipe) != len(ingredients):
        at_least_one_batch = False

    if at_least_one_batch == True:
        for x in recipe:
            print(recipe[x], "-- Recipe[x]")
            print(ingredients[x], " -- Ingredient[x]")
            batch = ingredients[x] // recipe[x]
            print(batch, "-- BATCH")
            

            if batch == 0:
                at_least_one_batch = False
            
            elif loops == 0 or max_batches >= batch:
                print(batch)
                max_batches = batch
                print(max_batches, "max batches")
                loops += 1
        print(max_batches)
        return max_batches
    
    else:
        return 0    
    

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 } 
  ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }

  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))