import cv2 as cv
import numpy as np
import random
import math

total = 0

def costs_calculate():

 for a in range(4):
    
    name = input("product name:")
    cost = float(input("product cost:"))

 print(name, "added")
 total += cost

 if (total < 1000 and total > 600):
    new_total = total * 0.8
 elif(total < 600 and total > 200):
    new_total = total * 0.75
 else:
    new_total = total

 print("Total costs: ", new_total)

costs_calculate()
